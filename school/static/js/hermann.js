$('#topmenu li a').click(function(e){

	var index = $(this).parent().index();
	childs = $('#topmenu').children();
	for (var i=0; i < childs.length; i += 1){
		if(childs[i].getAttribute('class') == 'active'){
			childs[i].setAttribute('class', '');
		} else {
			if (i == index){
				childs[i].setAttribute('class', 'active');
			}
		}
	}
	
});		
