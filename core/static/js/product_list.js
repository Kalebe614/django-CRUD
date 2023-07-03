// Start the product filter
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
// End the product filter

//Start the code to delete the product

    const modalTitle = document.querySelector('#deleteModal .modal-title');
    const modalBody = document.querySelector('#deleteModal .modal-body');
    const modal= document.getElementById("deleteModal");
    
    modal.addEventListener('hidden.bs.modal',function(){
        const form = modal.querySelector('form');
        form.reset();
        modalTitle.textContent =""
        modalBody.innerHTML =""
    });
    

    document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            
            const productId = this.getAttribute('data-product-id');
            const productName = this.getAttribute('data-product-name');
            const productPrice = this.getAttribute('data-product-price');

            const modalTitle = document.querySelector('#deleteModal .modal-title');
            const modalBody = document.querySelector('#deleteModal .modal-body');
            
            const deleteForm = document.getElementById('deleteForm');
            const url = `/delete/${productId}/`;
            deleteForm.setAttribute('action', url);

            modalTitle.textContent += `Delete Product: ${productName}`;
            modalBody.innerHTML += `
                <p id="msgAreYouSure">Are you sure you want to delete the product?</p>
                <p>Name: ${productName}</p>
                <p>Price: ${productPrice}</p>
            `;
        });
    });
});

