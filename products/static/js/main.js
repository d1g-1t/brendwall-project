document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('product-form');
    const tableBody = document.getElementById('product-table').querySelector('tbody');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const description = document.getElementById('description').value;
        const price = document.getElementById('price').value;

        fetch('/api/products/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, description, price }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.id) {
                loadProducts();
            } else {
                alert('Error: ' + JSON.stringify(data));
            }
        });
    });

    function loadProducts() {
        fetch('/api/products/')
            .then(response => response.json())
            .then(data => {
                tableBody.innerHTML = '';
                data.forEach(product => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${product.name}</td>
                        <td>${product.description}</td>
                        <td>${product.price}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });
    }

    loadProducts();
});