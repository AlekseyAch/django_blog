(function($) {
    $(document).ready(function() {
        $('.inline-group').on('click', '.add-row a', function() {
            setTimeout(function() {
                // Ваш код для добавления логики добавления/удаления полей
            }, 100); // Пауза для обеспечения правильной инициализации нового поля
        });
    });
})(django.jQuery);
