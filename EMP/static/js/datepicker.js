$(document).ready(function datepick() {
        $(".startDate").datepicker({
            numberOfMonths: 1,
           
            onSelect: function (selected) {
                var dt = new Date(selected);
                dt.setDate(dt.getDate() + 1);
                $(".endDate").datepicker("option", "minDate", dt);
            }
        });
        $(".endDate").datepicker({
            numberOfMonths: 1,
           
            onSelect: function (selected) {
                var dt = new Date(selected);
                dt.setDate(dt.getDate() - 1);
                $(".startDate").datepicker("option", "maxDate", dt);
            }
        });
    });

$(document).ready(function () {
        $("#id_date_of_birth").datepicker({
            numberOfMonths: 1,
           
            onSelect: function (selected) {
                var dt = new Date(selected);
                dt.setDate(dt.getDate() + 1);
                $("#id_date_of_joining").datepicker("option", "minDate", dt);
            }
        });
        $("#id_date_of_joining").datepicker({
            numberOfMonths: 1,
           
            onSelect: function (selected) {
                var dt = new Date(selected);
                dt.setDate(dt.getDate() - 1);
                $("#id_date_of_birth").datepicker("option", "maxDate", dt);
            }
        });
    });