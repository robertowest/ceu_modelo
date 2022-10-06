

/*Anclas*/
	var hash = window.location.hash;
	if($(hash).parents('.tab').length && !$(hash).parents('.tab').hasClass('.active')){
		$('.tabs-elements .tab').removeClass('active');
		$(hash).parents('.tab').addClass('active');
		if($(hash).is('.acordeon')){
			if( $(hash).parents('.acordeon').length){
				$(hash).parents('.acordeon').find('> .tag').addClass('active');
				$(hash).parents('.acordeon').find('> .acordeon-box').slideDown(300);
			}
			$(hash).find('> .tag').addClass('active');
			$(hash).find('> .acordeon-box').slideDown(300);
		}
	}
	$('a[href^="#"]').on('click',function (e) {
		window.location.reload();
		// if($(this).attr('href').indexOf("#") > -1){
		// 	console.log( $(this).attr('href'));
		// }
	});
/*Global vars*/
	var showSubmenu = 1;
	var initialWindowWidth = window.innerWidth;
	jQuery(document).ready(function ($) {

/*functions*/
	var claerAjaxCache = function(){
		$.ajaxSetup({
			cache:false
		});
	};
	// DOM click outer header close the menu responsive
	$(document).on('click', function(event) {
		var w = window.innerWidth;
		if( $(event.target).closest('.submenu').length == 0 && w < 1024 && $(event.target).closest('header').length == 0){
			var scroll = $(window).scrollTop();
			if(scroll < 140){
				$('.submenu').parents('header').removeClass('fixed');
			}
			$('.submenu').stop().animate({'right': -400}, 500, function(){
				$(this).hide();
			});
			$('.ctrl-menu').removeClass('active');
			$('.submenu').parents('header').removeClass('activeSubmenu');
			showSubmenu= 1;
		}
		if ($(event.target).closest('.cover-lang').length == 0) {
		    $('.cover-lang .idioms').slideUp(300);
		}
	});
/*Hash nav*/
	// $('a[href^="#"]').on('click',function (e) {
	// 	e.preventDefault();
	// 	var target = this.hash,
	// 		$target = $(target);
	// 	$('html, body').stop().animate(
	// 		{'scrollTop': $target.offset().top },
	// 		700,
	// 		'swing'
	// 	);
	// });
	$('.next-module').on('click', function(event) {
		event.preventDefault();
		var $target = $(this).parents('.module').next('.module');
		$('html, body').stop().animate(
			{'scrollTop': $target.offset().top - $('.menu-header').innerHeight()},
			700,
			'swing'
		);
	});
/*Menu selection*/
	$('.menu li[data-menu]').on('mouseenter', function(event) {
		var w = window.innerWidth;
		if(w > 1024){
			if(!$(this).hasClass('active')){
				$(this).addClass('active');
				$(this).siblings('li').removeClass('active');
				$(this).parents('.menu').find('.search-icon').addClass('active');
				var focus = $(this).attr('data-menu');
				$(this).parents('.back-menu').addClass('back-color');
				$(this).parents('.back-menu').next('.submenu').removeAttr('style');
				$('.submenu div[data-menu="'+focus+'"]').siblings('div').stop().hide();
				if(focus=='' || focus == undefined){
					return;
				}
				$(this).parents('.back-menu').next('.submenu').stop().fadeIn(300);
				$('.submenu div[data-menu="'+focus+'"]').stop().fadeIn(500);
				if(focus=='busqueda'){
					$('.search-btn').focus();
				}
			}
		}
	});
	$('.back-menu').on('mouseleave', function(event) {
		var focus = $(this).find('li.active').attr('data-menu');
		if(focus=='' || focus == undefined){
			$('.menu li[data-menu],.menu .search-icon').removeClass('active');
			$(this).removeClass('back-color');
		}
	});
	$('.submenu').on('mouseleave', function(event) {
		var w = window.innerWidth;
		if(w > 1024){
			$(this).stop().slideUp(500,function(){
				$(this).removeAttr('style');
			});
			$(this).find('div[data-menu]').stop().fadeOut(500);
			$(this).prev('.back-menu').find('.menu li[data-menu],.menu .search-icon').removeClass('active');
			$(this).prev('.back-menu').removeClass('back-color');
		}
	});
	$('.select-lang').on('click', function (event) {
	    event.preventDefault();
	    $(this).next('.idioms').stop().slideToggle(300);
	});
/*menu responsive*/
	$('.ctrl-menu').on('click', function(event) {
		event.preventDefault();
		$(this).toggleClass('active');
		var h = window.innerHeight;
		var scroll = $(window).scrollTop();
		if(scroll < 140){
			$(this).parents('header').toggleClass('fixed');
		}
		$(this).parents('header').toggleClass('activeSubmenu');
		var minush = $('.back-menu').outerHeight();
		$('.submenu').css({'height':h-minush});
		if(showSubmenu == 1){
			$('.submenu').show();
			$('.submenu').stop().animate({'right': 0}, 500);
			showSubmenu = 0;
		}else if(showSubmenu == 0){
			$('.submenu').stop().animate({'right': -400}, 500, function(){
				$(this).hide();
			});
			showSubmenu = 1;
		}
	});
	$('.submenu .category').on('click', function(event) {
		event.preventDefault();
		$(this).toggleClass('active');
		$(this).next('.cover-tags').stop().slideToggle(300);
		$(this).parents('div[data-menu]').siblings('div[data-menu]').find('.category').removeClass('active');
		$(this).parents('div[data-menu]').siblings('div[data-menu]').find('.cover-tags').stop().slideUp(300);
	});
	$.each($('header .top-header ul > li'), function(index, val) {
		if($(val).parents('.left').length){
			$('.submenu .generic-links[data-menu="centros"] ul').append($(val).clone());
		}else if($(val).parents('.right').length){
		    if ($(val).find('.idioms').length || $(val).parents('.idioms').length) {
		        if ($(val).parents('.idioms').length) {
		            $('.submenu .generic-links[data-menu="idiomas"] ul').append($(val).clone())
		        }
		    } else {
		        $('.submenu .generic-links[data-menu="perfiles"] ul').append($(val).clone());
		    }
		}
	});
/*Menu add elements*/
	$.each($('.information-block .clone'),function(index, el) {
		$('.add-elements .center').append($(el).clone());
	});
/*Home Gallery*/
	$.each($('.gallery .slide'),function(index, val){
        var src = $(val).find('> img').attr('src');
        if (src != null) {
            $(val).css({
                'background-image': 'url(' + src + ')',
                'background-size': 'cover',
                'background-position': 'center center'
            });
        }
        else {
            $(val).css({
                'background-size': 'cover',
                'background-position': 'center center'
            });
        }
		$(val).find('> img').remove();
    });
   
	$('.gallery').slick({
		arrows: false,
		dots: true,
		infinite: true,
		speed: 600,
		slidesToShow: 1,
		autoplay: true,
		autoplaySpeed: 6000
	});
/*Charts*/
	$.each($('.chart'), function(index, val) {
		//canvas initialization
			var canvas = $(val)[0];
			var ctx = canvas.getContext('2d');
		//dimensions
			var W = canvas.width;
			var H = canvas.height;
			var degrees = 0;
		function init(){
				ctx.clearRect(0, 0, W, H);
			//Background 360 degree arc
				ctx.beginPath();
				ctx.strokeStyle = $(val).attr('data-bgcolor');
				ctx.lineWidth = 10;
				ctx.arc(W/2, 50, 40, 0, Math.PI*2, false); //you can see the arc now
				ctx.stroke();

			//Background 360 degree arc
				ctx.beginPath();
				ctx.strokeStyle = $(val).attr('data-bgcolor');
				ctx.lineWidth = 10;
				ctx.arc(W/2, 155, 65, 0, Math.PI*2, false); //you can see the arc now
				ctx.stroke();
		
			//Variables
				var radians = degrees * Math.PI / 180;
				ctx.beginPath();
				ctx.strokeStyle = $(val).attr('data-color');
				ctx.lineWidth = 10;
				ctx.arc(W/2, 50, 40, 0 - 90*Math.PI/180, radians - 90*Math.PI/180, false); //you can see the arc now
				ctx.stroke();

			//text
				ctx.fillStyle = '#575757';
				ctx.font = "26px UtopiaBold";
				text = Math.floor(degrees/360*100) + "%";
				text_width = ctx.measureText(text).width;
				ctx.fillText(text, W/2 - text_width/2, H);
		}


		function draw(){
			var total_degrees = ($(val).attr('data-percent')*360)/100;
			
			var difference = total_degrees - degrees;
			
			setInterval(function(){
				if(degrees < total_degrees){
					degrees++;
				}
				init();
			},100/difference);
			
		}
		draw();
	});
/*Module news inline-block*/
	var countModuleNewsItems = 0;
	if(window.innerWidth <= 900){
		countModuleNewsItems = 2;
	}else{
		countModuleNewsItems = 3;
	}
	$.each($('.module-news .item'), function(index, val) {
		if(index < countModuleNewsItems){
			setTimeout(function(){
				$(val).css({'display':'inline-block'}).addClass('zoomIn').removeClass('hide');
			}, 400*index);
		}
	});
	$('.module-news .plus').on('click', function(event) {
		event.preventDefault();
		if(!$(this).hasClass('reverse')){
			var number = 0;
			$.each($('.module-news .item'), function(index, val) {
				if($(val).is('.hide')){
					number += 1;
					setTimeout(function(){
						$(val).css({'display':'inline-block'}).removeClass('zoomOut hide').addClass('zoomIn change');
					}, 300*(number-1) );
				}
			});
			$(this).addClass('reverse');
		}else{
			var number = 0;
			$.each($('.module-news .item').get().reverse(), function(index, val) {
				if($(val).is('.change')){
					number += 1;
					setTimeout(function(){
						$(val).removeAttr('style').removeClass('change zoomIn').addClass('zoomOut');
						setTimeout(function() {
							$(val).addClass('hide');
						}, 300);
					}, 300*(number-1) );
				}
			});
			$(this).removeClass('reverse');
			$('html, body').stop().animate(
				{'scrollTop': $(this).parents('.module-news').offset().top - $('.menu-header').innerHeight()},
				700,
				'swing'
			);
		}
	});
/*Module experience inline-block*/
	if($('.module-experience').length){
		$.each($('.module-experience'), function(index, val) {
			var countModuleExperienceItems = 0;
			if(window.innerWidth <= 900){
				countModuleExperienceItems = 3;
			}else if(window.innerWidth <= 550){
				countModuleExperienceItems = 2;
			}else{
				if($(val).attr('data-showElements') != "" && $(val).attr('data-showElements') != undefined && isNaN($(val).attr('data-showElements')) == false){
					countModuleExperienceItems = parseInt($(val).attr('data-showElements'));
				}
				else{
					countModuleExperienceItems = 5;
				}
			}
			$.each($(val).find('.col'), function(index, val) {
				if(index < countModuleExperienceItems){
					setTimeout(function(){
						$(val).css({'display':'inline-block'}).addClass('zoomIn').removeClass('hide');
						setTimeout(function(){
							$(val).removeAttr('style');
						}, 400);
					}, 400*index);
				}
			});
		});
		$('.module-experience').on('click', '.plus',function(event) {
			event.preventDefault();
			if(!$(this).hasClass('reverse')){
				var number = 0;
				$.each($(this).parents('.module-experience').find('.col'), function(index, val) {
					if($(val).is('.hide')){
						number += 1;
						setTimeout(function(){
							$(val).css({'display':'inline-block'}).removeClass('zoomOut hide').addClass('zoomIn change');
							setTimeout(function(){
								$(val).removeAttr('style');
							}, 300);
						}, 300*(number-1) );
					}
				});
				$(this).addClass('reverse');
			}else{
				var number = 0;
				$.each($(this).parents('.module-experience').find('.col').get().reverse(), function(index, val) {
					if($(val).is('.change')){
						number += 1;
						setTimeout(function(){
							$(val).removeAttr('style').removeClass('change zoomIn').addClass('zoomOut');
							setTimeout(function() {
								$(val).addClass('hide');
							}, 300);
						}, 300*(number-1) );
					}
				});
				$(this).removeClass('reverse');
				$('html, body').stop().animate(
					{'scrollTop': $(this).parents('.module-experience').offset().top - $('.menu-header').innerHeight()},
					700,
					'swing'
				);
			}
		});
	}
/*Module events inline-block*/
	var countModuleEventsItems = 4;
	if(window.innerWidth <= 900){
		countModuleEventsItems = 2;
	}else{
		if($('.events-section').attr('data-showElements') != "" && $('.events-section').attr('data-showElements') != undefined && isNaN($('.events-section').attr('data-showElements')) == false){
			countModuleEventsItems = parseInt($('.events-section').attr('data-showElements'));
		}
		else{
			countModuleEventsItems = 4;
		}
	}
	$.each($('.events-section .item'), function(index, val) {
		if(index < countModuleEventsItems){
			setTimeout(function(){
				$(val).css({'display':'inline-block'}).addClass('zoomIn').removeClass('hide');
				setTimeout(function(){
					$(val).removeAttr('style');
				}, 400);
			}, 400*index);
		}
	});
	$('.module-events .plus').on('click', function(event) {
		event.preventDefault();
		if(!$(this).hasClass('reverse')){
			var number = 0;
			$.each($('.events-section .item'), function(index, val) {
				if($(val).is('.hide')){
					number += 1;
					setTimeout(function(){
						$(val).css({'display':'inline-block'}).removeClass('zoomOut hide').addClass('zoomIn change');
						setTimeout(function(){
							$(val).removeAttr('style');
						}, 300);
					}, 300*(number-1) );
				}
			});
			$(this).addClass('reverse');
		}else{
			var number = 0;
			$.each($('.events-section .item').get().reverse(), function(index, val) {
				if($(val).is('.change')){
					number += 1;
					setTimeout(function(){
						$(val).removeAttr('style').removeClass('change zoomIn').addClass('zoomOut');
						setTimeout(function() {
							$(val).addClass('hide');
						}, 300);
					}, 300*(number-1) );
				}
			});
			$(this).removeClass('reverse');
			$('html, body').stop().animate(
				{'scrollTop': $(this).parents('.module-events').offset().top - $('.menu-header').innerHeight()},
				700,
				'swing'
			);
		}
	});
/*Module division-section*/
	var countModuleDivision = 0;
	if(window.innerWidth <= 900){
		countModuleDivision = 2;
	}else{
		countModuleDivision = 3;
	}
	$.each($('.division-section .item'), function(index, val) {
		if(index < countModuleDivision){
			setTimeout(function(){
				$(val).css({'display':'block'}).addClass('zoomIn').removeClass('hide');
				setTimeout(function(){
					$(val).removeAttr('style');
				}, 400);
			}, 400*index);
		}
	});
	$('.division-section .plus').on('click', function(event) {
		event.preventDefault();
		if(!$(this).hasClass('reverse')){
			var number = 0;
			$.each($('.division-section .item'), function(index, val) {
				if($(val).is('.hide')){
					number += 1;
					setTimeout(function(){
						$(val).css({'display':'block'}).removeClass('zoomOut hide').addClass('zoomIn change');
						setTimeout(function(){
							$(val).removeAttr('style');
						}, 300);
					}, 300*(number-1) );
				}
			});
			$(this).addClass('reverse');
		}else{
			var number = 0;
			$.each($('.division-section .item').get().reverse(), function(index, val) {
				if($(val).is('.change')){
					number += 1;
					setTimeout(function(){
						$(val).removeAttr('style').removeClass('change zoomIn').addClass('zoomOut');
						setTimeout(function() {
							$(val).addClass('hide');
						}, 300);
					}, 300*(number-1) );
				}
			});
			$(this).removeClass('reverse');
			$('html, body').stop().animate(
				{'scrollTop': $(this).parents('.division-section').parents('.module').offset().top - $('.menu-header').innerHeight()},
				700,
				'swing'
			);
		}
	});
	if($('.division-section').length && initialWindowWidth > 900){
		var topBlockDS =  $('.list-information .top-block').offset().top - $('.division-section').offset().top;
		$('.division-section').find('.block').css({'margin-top':topBlockDS});
	}
/*Module accordeon list*/
	$.each($('.accordeon-list .accordeon-item'), function(index, val) {
		var back = $(val).attr('data-background');
		$(val).css({
			"background": "url('"+back+"') 50% 50% no-repeat",
			"background-size": "cover"
		});
	});
	$('.accordeon-list .accordeon-item').on('mouseenter', function(event) {
		if(window.innerWidth > 750){
			$(this).removeClass('small').addClass('big');
			$(this).siblings('.accordeon-item').removeClass('big').addClass('small');
			$($(this).find('.box')[0]).addClass('animated fadeInUp');
		}
	});
	$('.accordeon-list .accordeon-item').on('mouseleave', function(event) {
		if(window.innerWidth > 750){
			$(this).removeClass('small big');
			$(this).siblings('.accordeon-item').removeClass('small big');
			$($(this).find('.box')[0]).removeClass('animated fadeInUp');
		}
	});
/*Module activities*/
	var countModuleActivitiesItems = 4;
	if(window.innerWidth <= 900){
		countModuleActivitiesItems = 2;
	}else{
		if($('.activities-section').attr('data-showElements') != "" && $('.activities-section').attr('data-showElements') != undefined && isNaN($('.activities-section').attr('data-showElements')) == false){
			countModuleActivitiesItems = parseInt($('.activities-section').attr('data-showElements'));
		}
		else{
			countModuleActivitiesItems = 4;
		}
	}
	$.each($('.activities-section .box'), function(index, val) {
		if(index < countModuleActivitiesItems){
			setTimeout(function(){
				$(val).removeClass('hide').css({'display':'inline-block'}).addClass('zoomIn');
				setTimeout(function(){
					$(val).removeAttr('style');
				}, 400);
			}, 400*index);
		}
	});
	$('.activities-section .plus').on('click', function(event) {
		event.preventDefault();
		if( isNaN( parseFloat($('.activities-section').attr('data-showNextElements')))){
			if(!$(this).hasClass('reverse')){
				var number = 0;
				$.each($('.activities-section .box.hide'), function(index, val) {
					number += 1;
					setTimeout(function(){
						$(val).css({'display':'inline-block'}).removeClass('zoomOut hide').addClass('zoomIn change');
						setTimeout(function(){
							$(val).removeAttr('style');
						}, 300);
					}, 300*(number-1) );
				});
				$(this).addClass('reverse');
			}else{
				var number = 0;
				$.each($('.activities-section .box.change').get().reverse(), function(index, val) {
					number += 1;
					setTimeout(function(){
						$(val).removeAttr('style').removeClass('change zoomIn').addClass('zoomOut');
						setTimeout(function() {
							$(val).addClass('hide');
						}, 300);
					}, 300*(number-1) );
				});
				$(this).removeClass('reverse');
				$('html, body').stop().animate(
					{'scrollTop': $(this).parents('.module-events').offset().top - $('.menu-header').innerHeight()},
					700,
					'swing'
				);
			}
		}else{
			var nextCount = parseFloat($('.activities-section').attr('data-showNextElements'));
			if($('.activities-section .box.hide').length > 0 ){
				if($('.activities-section .box.hide').length <= nextCount ){
					$(this).addClass('reverse');
				}
				var number = 0;
				$.each($('.activities-section .box.hide'), function(index, val) {
					if(index < nextCount){
						number += 1;
						setTimeout(function(){
							$(val).css({'display':'inline-block'}).removeClass('zoomOut hide').addClass('zoomIn change');
							setTimeout(function(){
								$(val).removeAttr('style');
							}, 300);
						}, 300*(number-1));
					}
				});
			}else{
				$.each($('.activities-section .box.change').get().reverse(), function(index, val) {
					$(val).removeAttr('style').removeClass('change zoomIn').addClass('zoomOut');
					setTimeout(function() {
						$(val).addClass('hide');
					}, 300);
				});
				$(this).removeClass('reverse');
				$('html, body').stop().animate(
					{'scrollTop': $(this).parents('.module-events').offset().top - $('.menu-header').innerHeight()},
					700,
					'swing'
				);
			}
		}
	});
/*Video*/
	$.each($('.video-section') ,function(index, el) {
		var backgroundVideo = $(el).find('.back-video').attr('src');
		$(el).find('.back-video').remove();
		$(el).css({
			'background': 'url('+backgroundVideo+') no-repeat',
			'background-position': 'center',
			'background-size': 'cover'
		});
	});
	if($('.video-gallery').length){
		$('.video-gallery').slick({
			arrows: true,
			dots: false,
			infinite: true,
			speed: 600,
			slidesToShow: 1,
			autoplay: true,
			autoplaySpeed: 6000
		});
	}
/*Modalbox*/
	$('.close-modal,.modalbox').on('click', function(event) {
		if($(event.target).is('td')){
			$('.modalbox').fadeOut(500);
			var data = $(this).attr('data-modal');
		}else if($(event.target).is('.close-modal')){
			$(this).parents('.modalbox').fadeOut(500);
			var data = $(this).parents('.modalbox').attr('data-modal');
		}
		// $('body, html').removeClass('overhide');
		switch(data) {
			case 'video':
				$('.modalbox[data-modal="video"]').find('.iframe').remove();
				break;
			case 'modalImgSlide':
			case 'modalImgSlide1':
			case 'modalImgSlide2':
			case 'modalImgSlide3':
			case 'modalImgSlide4':
			case 'modalImgSlide5':
			case 'modalImgSlide6':
			case 'modalImgSlide7':
			case 'modalImgSlide8':
			case 'modalImgSlide9':
			case 'modalImgSlide10':
				setTimeout(function(){
					$('.modalbox[data-modal="'+data+'"] .slide-img').slick('unslick');
				},500)
				break;
			default:
				// console.log('NOTHING');
				break;
		}
	});
	$('.open-modal').on('click', function(event) {
		event.preventDefault();
		// $('body, html').addClass('overhide');
		var focus = $(this).attr('data-modal');
		$('.modalbox[data-modal="'+focus+'"]').fadeIn(300);
		if(focus == 'video'){
			var uri = $(this).attr('data-uri');
			var modalboxVideo = '<iframe class="iframe" src="'+uri+'" frameborder="0" allowfullscreen></iframe>'
			$('.modalbox[data-modal="video"]').find('.video').append(modalboxVideo);
		}
		if(focus == 'modalImg'){
			var uri = $(this).attr('data-bigImg');
			$('.modalbox[data-modal="modalImg"]').find('.cover-img img').attr('src', uri);
		}
		if(focus == 'modalImgSlide' || focus == 'modalImgSlide1' || focus == 'modalImgSlide2' || focus == 'modalImgSlide3' || focus == 'modalImgSlide4' || focus == 'modalImgSlide5' || focus == 'modalImgSlide6' || focus == 'modalImgSlide7' || focus == 'modalImgSlide8' || focus == 'modalImgSlide9' || focus == 'modalImgSlide10'){
			var index = $(this).parents('.thumbs').index();
			$('.modalbox[data-modal="'+focus+'"] .slide-img').slick({
				arrows: true,
				dots: false,
				infinite: true,
				speed: 600,
				slidesToShow: 1,
				autoplay: false,
				autoplaySpeed: 6000,
				initialSlide: index,
				adaptiveHeight: true
			});
		}
	});
	$('.open-internal').on('click', function(event) {
		event.preventDefault();
		$(this).parents('.modalbox').find('.internal-modal').fadeIn(300);
	});
/*Scroll action*/
	var infoBlockTop =  200;
	function stick_relocate(){
		var scroll = $(window).scrollTop();
		var w = window.innerWidth;
		if(scroll >= 140 ){
			$('header').addClass('fixed animated half fadeInDownBig');
		}else{
			if(!$('header').hasClass('activeSubmenu')){
				$('header').removeClass('fixed animated half fadeInDownBig');
			}
		}

		/*information block*/
        if (window.innerWidth > 414 && $('.information-block').length){
				$('.back-menu .add-elements').css('bottom', - $('.back-menu .add-elements').outerHeight());

				if(scroll >= infoBlockTop){
					$('.back-menu .add-elements').show().addClass('animated half flipInX');
					$('header.fixed .menu-header').css('box-shadow', 'none');
				}else {

					$('.back-menu .add-elements').hide().removeClass('animated half flipInX');
					$('header.fixed .menu-header').removeAttr('style');
				}
			}
			// if($('.information-block').length){
			// 	var infoBlockTop = $('.module.next-section').offset().top - $('.menu-header').height() +40;
			// 	if(scroll >= infoBlockTop && !$('.information-block').hasClass('fixed')){
			// 		var htop = $('header.fixed .menu-header .back-menu').outerHeight() > 97 ? 97:$('header.fixed .menu-header .back-menu').outerHeight();
			// 		$('.information-block').css('top', htop).addClass('fixed animated half flipInX');
			// 		$('header.fixed .menu-header').css('box-shadow', 'none');
			// 	}else if(scroll < infoBlockTop){
			// 		$('.information-block').removeClass('fixed animated half flipInX').removeAttr('style');
			// 		$('header.fixed .menu-header').removeAttr('style');
			// 	}
			// }
	}
	$(window).scroll(stick_relocate);

	var windowWidth = window.innerWidth;
	if(windowWidth < 900 && $('.Iscroll').length){
		var myScroll;
		function loadedScroll () {
			myScroll = new IScroll('.Iscroll', { scrollX: true, freeScroll: true, click:true });
		}
		loadedScroll();
	}

	if($('.cover-calendar .cover-days').length){
		var myScroll;
		function loadedScroll2 () {
			myScroll = new IScroll('.cover-calendar .cover-days', { scrollX: true, freeScroll: true, click:true });
		}
		loadedScroll2();
		console.log('asd')
	}
    /*datepicker*/
    //if($('.datepicker').length){
    //	$('.datepicker').datepicker({
    //		dateFormat: 'dd/mm/yy',
    //		monthNames: ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    //		dayNames: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "SÃ¡bado"],
    //		dayNamesMin: ["D","L","M","X","J","V","S"]
    //	});
    //}
    //if($('.datepicker-from').length){
    //	$('.datepicker-from').datepicker({
    //		dateFormat: 'dd/mm/yy',
    //		monthNames: ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    //		dayNames: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "SÃ¡bado"],
    //		dayNamesMin: ["D","L","M","X","J","V","S"],
    //		onClose: function(selectedDate) {
    //			$('.datepicker-to').datepicker("option","minDate", selectedDate);
    //		}
    //	});
    //}
    //if($('.datepicker-to').length){
    //	$('.datepicker-to').datepicker({
    //		dateFormat: 'dd/mm/yy',
    //		monthNames: ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    //		dayNames: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "SÃ¡bado"],
    //		dayNamesMin: ["D","L","M","X","J","V","S"],
    //		onClose: function(selectedDate) {
    //			$('.datepicker-from').datepicker("option","maxDate", selectedDate);
    //		}
    //	});
    //}
    /*filepicker*/
	var file_txt = $('.input-file-picker').text();
	$('.input-file-picker').on('click', function(event) {
		event.preventDefault();
		$(this).prev('input[type="file"].form-ctrl').trigger('click');
	});
	$('input[type="file"].form-ctrl').on('change', function(event) {
		event.preventDefault();
		var focus = $(this).next('.input-file-picker');
		$(focus).html($(this)[0].files[0].name+'<i class="remove"></i>');
	});
	$('.input-file-picker').on('click', '.remove', function(event) {
		event.preventDefault();
		$('.input-file-picker').html(file_txt+'<i></i>');
	});
/*Calendar action*/
	$('.cover-calendar .cover-days').on('click', 'li',function(event) {
		$(this).siblings('li').removeClass('active');
		$(this).addClass('active');
	});
/*Acordeon*/
	$(document).on('click', '.cover-acordeon .tag',function(event) {
		event.preventDefault();
		$(this).toggleClass('active');
		$(this).next('.acordeon-box').stop().slideToggle(300);
		$(this).closest('.acordeon').siblings('.acordeon').find('.tag').removeClass('active');
		$(this).closest('.acordeon').siblings('.acordeon').find('.acordeon-box').removeClass('active').slideUp(300);
	});
	if($('.cover-acordeon .tag').is('.active')){
		$('.cover-acordeon .tag.active').next('.acordeon-box').slideDown(300);
	}
/*Tabs*/
	$('.tabs-navigation .tab-ctrl').on('click', function(event) {
	    event.preventDefault();

	    if ($(this).hasClass('active')) { return; }
		$(this).addClass('active');
		$(this).siblings('.tab-ctrl').removeClass('active');
		var ind_ = $(this).index();
		var focus = $(this).parents('.tabs-navigation').attr('data-action');
		$('.tabs-elements[data-action="'+focus+'"]').find('.tab:eq('+ind_+')').addClass('active');
		$('.tabs-elements[data-action="'+focus+'"]').find('.tab:eq('+ind_+')').siblings('.tab').removeClass('active');
		var $target = $('.tabs-elements[data-action="'+focus+'"] .tab.active');
		//$('html, body').stop().animate(
		//	{'scrollTop': $target.offset().top - $('.menu-header').innerHeight()},
		//	700,
		//	'swing'
		//);
		if($('.dynamic-title').length){
			var txt = $(this).find('span').text();
			$('.dynamic-title').text(txt);
		}
	});
/*Code show*/
	$('.view-code').on('click', function(event) {
		event.preventDefault();
		$(this).next('code').stop().slideToggle();
	});
/*Box hover effect*/
	$('.block-hover-info').on('mouseenter', '.box-hov', function(event) {
		event.preventDefault();
		$(this).find('.front-info').addClass('fadeOut');
		$(this).find('.back-info').removeClass('fadeOut').addClass('flipInX');
	});
	$('.block-hover-info').on('mouseleave', '.box-hov', function(event) {
		event.preventDefault();
		$(this).find('.front-info').removeClass('fadeOut');
		$(this).find('.back-info').removeClass('flipInX').addClass('fadeOut');
	});
/*Comment Gallery*/
	if($('.comment-gallery').length && $('.comment-gallery').hasClass('small')){
		$('.comment-gallery.small').slick({
			arrows: true,
			dots: false,
			infinite: true,
			speed: 600,
			slidesToShow: 1,
			autoplay: true,
			autoplaySpeed: 5000
		});
	}
	else if ($('.comment-gallery').length && $('.comment-gallery').hasClass('testimonios-master')) {
		$('.comment-gallery').slick({
			arrows: true,
			dots: false,
			infinite: true,
			speed: 600,
			slidesToShow: 1,
			autoplay: true,
			autoplaySpeed: 12000
		});
	}
	else if ($('.comment-gallery').length) {
	    $('.comment-gallery').slick({
	        arrows: true,
	        dots: false,
	        infinite: true,
	        speed: 600,
	        slidesToShow: 1,
	        autoplay: true,
	        autoplaySpeed: 3000
	    });
	}
	// $('.comment-gallery').on('beforeChange', function(event, slick, currentSlide, nextSlide){
	// 	$('.comment-gallery').find('.img-block').removeClass('fadeIn').addClass('fadeOut');
	// 	$('.comment-gallery').find('.description-block').removeClass('fadeIn').addClass('fadeOut');
	// });
	// $('.comment-gallery').on('afterChange', function(event, slick, currentSlide, nextSlide){
	// 	$('.comment-gallery').find('.slick-current .img-block').removeClass('fadeOut').addClass('fadeIn');
	// 	$('.comment-gallery').find('.slick-current .description-block').removeClass('fadeOut').addClass('fadeIn');
	// });
/*Options Gallery*/
	$('.options-gallery').slick({
		arrows: false,
		dots: false,
		infinite: true,
		speed: 600,
		slidesToShow: 1,
		rows: 8,
		autoplay: true,
		autoplaySpeed: 6000,
		responsive: [{
			breakpoint: 900,
			settings: {
				arrows: false,
				slidesToShow: 1,
				rows: 4
			}
		},{
			breakpoint: 550,
			settings: {
				arrows: false,
				slidesToShow: 1,
				rows: 2
			}
		}]
	});
/*areas*/
	$('.areas li').hover(function() {
		$(this).siblings('li').addClass('opacity');
		$(this).siblings('li.active').removeClass('opacity')
		if($('.areas .active').length)
			$(this).removeClass('opacity')
	}, function() {
		if(!$('.areas .active').length)
			$(this).siblings('li').removeClass('opacity');
		else if(!$(this).hasClass('active'))
			$(this).addClass('opacity')
	});
	$('.areas li').on('click', function(event) {
		event.preventDefault();
		if($(this).hasClass('active')){
			$(this).removeClass('active opacity');
			$(this).siblings('li').removeClass('opacity');
			$('.areas-content [data-area]').hide();
		}else{
			$(this).siblings('li').removeClass('active').addClass('opacity');
			$(this).removeClass('opacity').addClass('active').removeAttr('style');
			var focus = $(this).attr('data-area');
			$('.areas-content [data-area]').hide();
			$('.areas-content [data-area="'+focus+'"]').fadeIn();
		}
	});
/*description table*/
	if($('.description-table').length){
		$.each($('.description-table .body-info .cdu'), function(index, val) {
			$(val).prepend($('.description-table .head-info .cdu .show').clone(true));
		});
		$.each($('.description-table .body-info .content'), function(index, val) {
			$(val).prepend($('.description-table .head-info .content .show').clone(true));
		});
		$.each($('.description-table .body-info .room'), function(index, val) {
			$(val).prepend($('.description-table .head-info .room .show').clone(true));
		});
	}
/*links on buttons*/
	$(document).on('mouseleave', '.clone', function(event) {
		event.preventDefault();
		$(this).find('.links-elements').stop().hide();
	});
	$(document).on('mouseleave', '.links-elements', function(event) {
		event.preventDefault();
		$(this).stop().hide();
	});
	$(document).on('mouseenter', '.hover-action', function(event) {
		event.preventDefault();
		if( $(event.target).is('.hover-action')){
			$('.links-elements').hide();
			$(this).next('.links-elements').stop().show();
		}
	});
/*results-box*/
	if($('.results-box .box').length){
		$.each($('.results-box .box'), function(index, val){
			var src = $(val).find('img').attr('src');
			$(val).find('figure').css({'background':'url('+src+')','background-position':'center center','background-size':'cover'});
			$(val).find('img').remove();
		});
	}
/*portlet*/
	$('.portlet .portlet-title .collapse').on('click', function(event) {
		event.preventDefault();
		$(this).parents('.portlet-title').next('.portlet-body').slideToggle(300);
	});
/*tooltip*/
	//$('[data-toggle="tooltip"]').tooltip();
/*Multiselect*/
	if($('.form-ctrl.multiselect').length){
		$('.form-ctrl.multiselect').multiselect();
	}
/*form steps*/
	if($('.form-steps').length){
		$('.form-steps').css('width', $('.form-steps .step').length*100+'%');
		$('.form-steps .step').each(function(index, el) {
			var _w =  100/$('.form-steps .step').length;
			$(el).css({'width': _w+'%'});
		});

		$('.form-steps .next-step').on('click', function(event) {
			event.preventDefault();
			$(this).parents('.form-steps').animate({'left': '-=100%'},300);
			console.log($(this).parents('.form-steps'));
		});
		$('.form-steps .prev-step').on('click', function(event) {
			event.preventDefault();
			$(this).parents('.form-steps').animate({'left': '+=100%'},300);
		});
	}
/*residence*/
	$(document).on('click', '.residence-list .residence-box .btn', function(event) {
		if(!$(this).hasClass('link')){
			event.preventDefault();
			var ind_ = $(this).parents('.residence-box').index();
			$(this).parents('.residence-list').hide();
			$(this).parents('.residence-list').next('.residence-detail').show();
			$('.residence-detail').find('.detail-box:eq('+ind_+')').fadeIn(300);
		}
	});
	$('.residence-detail .back').on('click', function(event) {
		event.preventDefault();
		$(this).parents('.residence-detail').hide().find('.detail-box').hide();
		$(this).parents('.residence-detail').prev('.residence-list').fadeIn(300);
	});
/*admission*/
	$('.select-panel-admission').on('click', '.next-step', function(event) {
		event.preventDefault();
		if($('.dni').val() == "" && $('.passport').val() == ""){
			return;
		}
		if($('.dni').val() != ""){
			var fill = "nacional";
		}else if($('.passport').val() != ""){
			var fill = "internacional";
		}else {
			var fill = "";
		}
		$('.nav-admission').find('.step.active').removeClass('active').next().addClass('active');
		$(this).parents('.step').removeClass('active');
		if($(this).parents('.step').next().is('.nacional') || $(this).parents('.step').next().is('.internacional')){
			if(fill == "nacional"){
				console.log(fill);
				$('.select-panel-admission .step.nacional').addClass('active');
			}else if(fill == "internacional"){
				$('.select-panel-admission .step.internacional').addClass('active');
			}else{
				$('.select-panel-admission .step:eq(0)').addClass('active')
			}
		}else{
			$(this).parents('.step').next().addClass('active');
		}
	});
/*maps*/
	if ($('#maps-luis-campos').length) {
		function initializeMaps1() {
			var mapOptions = {
				scaleControl: true,
				scrollwheel: false,
				zoom: 17,
				center: new google.maps.LatLng(39.547248, -0.386797),
				mapTypeControlOptions: {
					mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
				}
			};

			map = new google.maps.Map(document.getElementById('maps-luis-campos'),
			mapOptions);
			var iconurl = 'img/map-icon.png'
			var marker = new google.maps.Marker({
				map: map,
				icon: iconurl,
				scale: 1,
				position: new google.maps.LatLng(39.547248, -0.386797)
			});
			panorama = map.getStreetView();
			panorama.setPosition(new google.maps.LatLng(39.547248, -0.386797));
			panorama.setPov(/** @type {google.maps.StreetViewPov} */({
				heading: 265,
				pitch: 0
			}));
		}

		function streetView(){
			panorama.setVisible(true);
		}
		initializeMaps1();
	}
	if ($('#gmaps').length) {
		var latitud = $('#gmaps').attr('data-lat');
		var longitud = $('#gmaps').attr('data-lng');
		function initializeMaps2(lat,lng) {
			lat = Number(lat);
			lng = Number(lng);
			var mapOptions = {
				scaleControl: true,
				scrollwheel: false,
				zoom: 17,
				center: new google.maps.LatLng(lat, lng),
				mapTypeControlOptions: {
					mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
				}
			};

			map = new google.maps.Map(document.getElementById('gmaps'),
			mapOptions);
			var iconurl = 'img/map-icon.png'
			var marker = new google.maps.Marker({
				map: map,
				icon: iconurl,
				scale: 1,
				position: new google.maps.LatLng(lat, lng)
			});
			panorama = map.getStreetView();
			panorama.setPosition(new google.maps.LatLng(lat, lng));
			panorama.setPov(/** @type {google.maps.StreetViewPov} */({
				heading: 265,
				pitch: 0
			}));
		}

		function streetView(){
			panorama.setVisible(true);
		}
		initializeMaps2(latitud,longitud);
		var boolmap = true;
		$(document).on('click', function(event) {
			if($('#gmaps').length && $('#gmaps').is(':visible') && boolmap == true){
				initializeMaps2(latitud,longitud);
				boolmap = false;
			}
		});
	}
/*acordeon-box display acordeon*/
	if($('.acordeon-box.hide-acordeon').length){
		$.each($('.acordeon-box.hide-acordeon'), function(index, val) {
			var number = $(val).attr('data-acordeonShow');
			$.each($(val).find('.acordeon'), function(index, val) {
				if(index < number){
					$(val).show();
				}
			});
		});
		$('.acordeon-box.hide-acordeon .plus').on('click', function(event) {
			event.preventDefault();
			var number = Number($(this).parents('.acordeon-box.hide-acordeon').attr('data-acordeonShow')) + Number($(this).parents('.acordeon-box.hide-acordeon').find('.acordeon:visible').length);
			console.log(number);
			$.each($(this).parents('.acordeon-box.hide-acordeon').find('.acordeon'), function(index, val) {
				if(!$(val).is(':visible')){
					if(index < number){
						$(val).show();
					}
				}
			});
		});
	}
/*Chronology*/
	if($('.mask-chronology').length){
		// for (var i = 0; i <= 3; i++) {
		// 	$('.mask-chronology ul').append('<li class="offset"><div class="date"><span class="year">clear</span><span class="point"></span></div></li>')
		// }
		// $('.mask-chronology ul').width($('.mask-chronology li').length * $('.mask-chronology li').innerWidth());
	}
	$('.mask-chronology').on('click', '.point', function(event) {
		event.preventDefault();
		$(this).parents('li').siblings('li').removeClass('active');
		$(this).parents('li').addClass('active');
		var left = $(this).parents('li').index() * $(this).parents('li').innerWidth();
		$('.mask-chronology').animate({scrollLeft: left}, 300);
	});
	$('.chronology .arrow-right').on('click', function(event) {
		event.preventDefault();
		var left = $(this).prev('.mask-chronology').innerWidth();
		if(($(this).prev('.mask-chronology').scrollLeft() + left) > ($(this).prev('.mask-chronology').find('li').length * $(this).prev('.mask-chronology').find('li').innerWidth())){
			return;
		}
		$(this).prev('.mask-chronology').animate({scrollLeft: '+='+left}, 300);
	});
	$('.chronology .arrow-left').on('click', function(event) {
		event.preventDefault();
		var left = $(this).next('.mask-chronology').innerWidth();
		$(this).next('.mask-chronology').animate({scrollLeft: '-='+left}, 300);
	});
});
$(window).on('load', function(event) {

});
$(window).on('resize', function(event) {
	var w = window.innerWidth;
	if( initialWindowWidth != w ){
		if(w >= 1024){
			$('header, header *, header .submenu').removeAttr('style');
			$('header .ctrl-menu').removeClass('active');
			$('header').removeClass('activeSubmenu');
			showSubmenu = 1;
		}else{
			$('header .ctrl-menu').removeClass('active');
			$('header, header *').removeAttr('style');
			$('header').removeClass('activeSubmenu');
			showSubmenu = 1;
			var scroll = $(window).scrollTop();
			if(scroll < 140){
				$('header').removeClass('fixed animated half fadeInDownBig');
			}
		}
	}
});
/* BUSCADOR DE LA HOME */
