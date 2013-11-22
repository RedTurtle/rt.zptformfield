/**
 * Helper JS for rt.zptformfield lines field
 */

(function($) {

	$(document).ready(function() {
		
		$('.zptformfield .linesAdd').click(function(event) {
			event.preventDefault();
			var container = $(this).closest('.zptformfield');
			var field = $('.newLinesField', container);
			if (!$.trim(field.val())) {
				return;
			} else if (field.attr('pattern')) {
				var pattern = new RegExp(field.attr('pattern'));
				if (!pattern.test(field.val())) {
					return false
				}
			}
			var newFieldRow = $('.fieldModel li', container).clone(true);
			var newField = newFieldRow.find('input');
			var fieldName = container.data('fieldname');
			newField.prop('name', fieldName+':list');
			newField.val(field.val());
			newFieldRow.find('strong').text(field.val());
			field.val('');
			field.focus();
			$('.fieldValues', container).append(newFieldRow);
			
		}).keypress(function(event) {
			if (event.which === 13) {
				event.preventDefault();
				$(this).click();
			}
		});
		
		$('.zptformfield .deleteItem').click(function(event){
			event.preventDefault();
			$(this).closest('li').remove();
		});
		
	});

})(jQuery);