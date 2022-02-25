(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });


    // Progress Bar
    $('.pg-bar').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Calender
    $('#calender').datetimepicker({
        inline: true,
        format: 'L'
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
        nav : false
    });

// testing my charts from github

var chartData = {
    labels: JSON.parse(jinjaLabels),
    
    datasets: [{
      data: JSON.parse(jinjaValues),
      label: jinjaLegend,
      backgroundColor: "#50164F63",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "#164F63",
      pointRadius: 1,
      pointHitRadius: 10
      }]
  }
  
  console.log(jinjaLabels);
  console.log(jinjaValues);
  
  
  // get chart canvas
  var ctx = document.getElementById("myChart").getContext("2d");
  
  // create the chart using the chart canvas
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: chartData,
  });




// var ctx = document.getElementById("myChartnew");
// var myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ["NG", "OK"],
//         datasets: [{
//             label: 'Those are colors',
//             data: [12, 19, 3, 5, 2, 3]
//         }]
//     },
//     });




 


    
})(jQuery);

