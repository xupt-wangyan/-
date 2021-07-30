var TaskList = function () {

    return {

        initTaskWidget: function () {
			$('input.main_list-child').change(function() {
				if ($(this).is(':checked')) { 
					$(this).parents('li').addClass("task-done"); 
				} else { 
					$(this).parents('li').removeClass("task-done"); 
				}
			}); 
        }

    };

}();