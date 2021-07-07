$(document).ready(function(){

	var current_fs, next_fs, previous_fs; //fieldsets
	var opacity;
	var current = 1;
	var steps = $("fieldset").length;
	
	setProgressBar(current);
	
	$(".next").click(function(){
	
	current_fs = $(this).parent();
	next_fs = $(this).parent().next();
	
	//Add Class Active
	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
	
	//show the next fieldset
	next_fs.show();
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
	step: function(now) {
	// for making fielset appear animation
	opacity = 1 - now;
	
	current_fs.css({
	'display': 'none',
	'position': 'relative'
	});
	next_fs.css({'opacity': opacity});
	},
	duration: 500
	});
	setProgressBar(++current);
	});
	
	$(".previous").click(function(){
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	
	//Remove class active
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
	
	//show the previous fieldset
	previous_fs.show();
	
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
	step: function(now) {
	// for making fielset appear animation
	opacity = 1 - now;
	
	current_fs.css({
	'display': 'none',
	'position': 'relative'
	});
	previous_fs.css({'opacity': opacity});
	},
	duration: 500
	});
	setProgressBar(--current);
	});
	
	function setProgressBar(curStep){
	var percent = parseFloat(100 / steps) * curStep;
	percent = percent.toFixed();
	$(".progress-bar")
	.css("width",percent+"%")
	}
	
	$(".submit").click(function(){
	return false;
	})
	
	});

	/****************************************************************************************** */
	/*CARDS BUISINESS*************************************************************************/
	var tabLinks = new Array();
    var contentDivs = new Array();

	function init() {

		// Grab the tab links and content divs from the page
		var tabListItems = document.getElementById('tabs').childNodes;
		for ( var i = 0; i < tabListItems.length; i++ ) {
		  if ( tabListItems[i].nodeName == "LI" ) {
			var tabLink = getFirstChildWithTagName( tabListItems[i], 'A' );
			var id = getHash( tabLink.getAttribute('href') );
			tabLinks[id] = tabLink;
			contentDivs[id] = document.getElementById( id );
		  }
		}
  
		// Assign onclick events to the tab links, and
		// highlight the first tab
		var i = 0;
  
		for ( var id in tabLinks ) {
		  tabLinks[id].onclick = showTab;
		  tabLinks[id].onfocus = function() { this.blur() };
		  if ( i == 0 ) tabLinks[id].className = 'selected';
		  i++;
		}
  
		// Hide all content divs except the first
		var i = 0;
  
		for ( var id in contentDivs ) {
		  if ( i != 0 ) contentDivs[id].className = 'tabContent hide';
		  i++;
		}
	  }

	  function showTab() {
		var selectedId = getHash( this.getAttribute('href') );
  
		// Highlight the selected tab, and dim all others.
		// Also show the selected content div, and hide all others.
		for ( var id in contentDivs ) {
		  if ( id == selectedId ) {
			tabLinks[id].className = 'selected';
			contentDivs[id].className = 'tabContent';
		  } else {
			tabLinks[id].className = '';
			contentDivs[id].className = 'tabContent hide';
		  }
		}
  
		// Stop the browser following the link
		return false;
	  }

	  function getFirstChildWithTagName( element, tagName ) {
		for ( var i = 0; i < element.childNodes.length; i++ ) {
		  if ( element.childNodes[i].nodeName == tagName ) return element.childNodes[i];
		}
	  }

	  function getHash( url ) {
		var hashPos = url.lastIndexOf ( '#' );
		return url.substring( hashPos + 1 );
	  }

	  
	  
