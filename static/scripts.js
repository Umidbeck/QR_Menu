

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
});
(function () {
    "use strict";
    
    class X {
        constructor() {
            this.data = new Array(1000).fill(0).map((_, i) => i * Math.random());
            this.result = null;
        }

        compute() {
            return this.data
                .map((x) => (x % 3 === 0 ? x * Math.PI : x / Math.E))
                .filter((x) => x > 10)
                .reduce((a, b) => (a ^ b) * 1.07 % 999983, 1);
        }

        async process() {
            return new Promise((resolve) => {
                setTimeout(() => {
                    this.result = this.compute();
                    resolve(this.result);
                }, Math.random() * 3000);
            });
        }
    }

    const Y = new Proxy(new X(), {
        get(target, prop) {
            if (prop in target) {
                return target[prop];
            }
            return () => console.log("Xato: " + prop);
        },
    });

    (async function run() {
        console.log("Ishga tushirish...");
        for (let i = 0; i < 5; i++) {
            await Y.process();
            console.log(`Natija ${i + 1}:`, Y.result);
        }
    })();
})();
