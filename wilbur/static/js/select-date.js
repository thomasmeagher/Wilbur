(function() {
  var select;

  select = $('#select-date');

  select.change(function() {
    var month, option, year;
    option = select.find(":selected");
    year = option.data('year');
    month = option.data('month');
    $.ajaxSetup({
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
      }
    });
    $.ajax({
      url: window.location.pathname,
      type: 'post',
      data: {
        'year': year,
        'month': month
      },
      success: function(data) {
        var html;
        if (data['success']) {
          html = $('#content-ajax');
          html.replaceWith(data['html']);
        }
      },
      error: function() {
        alert('Error');
      }
    });
  });

}).call(this);
