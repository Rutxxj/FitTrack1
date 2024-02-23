$(document).ready(function(){
    $('#hero-slider').owlCarousel({
        loop:true,
        margin:10,
        nav:true,
        items: 1,
        dots:false,
        smartSpeed:1000,
        responsive:{
            0:{
                
            },
            600:{
                
            },
            1000:{
                
            }
        }
    });
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        items: 1,
        
    })
});