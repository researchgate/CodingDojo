$(function() {
  var toggleCell = function(e) {
    if(event.which == 1) {
      $(this).toggleClass('selected');
      sendRequest();
    }
  };

  var sendRequest = function(e) {
    var data = '100-';

    $('.cell').each(function() {
      if ($(this).hasClass('selected')) {
        data = data + '1';
      } else {
        data = data + '0';
      }
    });

    console.log(data.length);

    $.ajax({
      url: 'http://localhost:8080',
      data: data,
      type: 'POST',
      // dataType: 'json',
      crossDomain: true,
      success: function() { console.log('Success'); },
      error: function() { console.log('Failed'); },
      headers: {
        // 'Content-Length': data.length
      }
    });
  };

  for (var i = 0; i < 16; i++) {
    $('.canvas').append('<div class="cell" />');
  }

  $('.cell').on('mouseenter', toggleCell);

  $('.submit').on('click', function() {

    // console.log(data.length);

    // $.post('http://192.168.178.134:8080', data);

  });
});
