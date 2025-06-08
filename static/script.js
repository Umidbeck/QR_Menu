document.querySelector('.lang-btn').addEventListener('click', function() {
    alert("Tilni o'zgartirish funksiyasi qo'shiladi!");
});
document.querySelectorAll('.category').forEach(item => {
    item.addEventListener('click', function() {
        alert(this.innerText + " bo‘limi tanlandi!");
    });
});
// script.js
function showSection(sectionId) {
    document.querySelectorAll('.section').forEach(section => {
        section.style.display = 'none';
    });
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('active');
    });
    document.getElementById(sectionId).style.display = 'block';
    document.querySelector(`[onclick="showSection('${sectionId}')"]`).classList.add('active');
}



document.addEventListener('DOMContentLoaded', function () {
    const categoryButtons = document.querySelectorAll('.categories button');
    const productCategories = document.querySelectorAll('.product-category');

    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Faqat bosilgan kategoriyani ko'rsatish
            const targetCategory = button.getAttribute('data-category');
            productCategories.forEach(category => {
                if (category.id === targetCategory) {
                    category.classList.add('active');
                } else {
                    category.classList.remove('active');
                }
            });

            // Tugmalarni aktiv holatga o'tkazish
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });
});3