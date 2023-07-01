function filterProducts() {
    const searchInput = document.getElementById('search-input');
    const productList = document.getElementById('product-list');
    const items = Array.from(productList.getElementsByClassName('table-active'));

    const searchTerm = searchInput.value.toLowerCase();

    items.forEach(item => {
    const productName = item.getElementsByTagName('td')[1].textContent.toLowerCase();
        if (productName.includes(searchTerm)) {
            item.style.display = 'table-row';
        } else {
            item.style.display = 'none';
            }
    });
}

const searchInput = document.getElementById('search-input');
searchInput.addEventListener('keyup', filterProducts);
