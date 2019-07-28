$(".alerto").click(function (event) {
    $.confirm({
        content: function () {
            var self = this;
            return $.ajax({
                type: 'POST',
                url: "{% url 'validate_amount' %}",
                dataType: 'json',
            }).done(function (response) {
                self.setContent('Description: ' + response.description);
                self.setContentAppend('<br>Version: ' + response.version);
                self.setTitle(response.name);
            }).fail(function () {
                self.setContent('Something went wrong.');
            });
        }
    });


    $.confirm({
        content: function () {
            var self = this;
            return $.ajax({
                url: "{% url 'validate_amount' %}",
                dataType: 'json',
                method: 'get'
            }).done(function (data) {
                self.setContent('Description: ' + data.description);
                self.setContentAppend('<br>Version: ' + data.balance_msg);
                self.setTitle(data.balance_msg);
                $("#exampleModal").modal('toggle');
            }).fail(function(){
                self.setContent('Something went wrong.');
                $("#exampleModal").modal('toggle');
            });
        }
    });
});