$(document).ready(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#my_modal .modal-content").html("");
                $("#my_modal").modal("show");
            },
            success: function (data) {
                $("#my_modal .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        // debugger
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#datatable_responsive_attendance tbody").html(data.html_book_list);
                    $("#my_modal").modal("hide");
                }
                else {
                    $("#my_modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    /* create */
    $(".attendance-btn").click(loadForm);
    $("#my_modal").on("submit", ".add_attendance", saveForm);
    
    /* update */
    $("#datatable_responsive_attendance").on("click", ".profile-btn", loadForm);
    $("#my_modal").on("submit", ".update_attendance", saveForm);

});