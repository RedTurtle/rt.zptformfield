/**
 * Trigger the Plone browserreferencefield features
 */

(function($) {
    if (!window.referenceBrowserLoaded) {
        $(document).ready(function() {

            /**
             * Remove selected reference
             */
            $('.removeReference').click(function(event) {
                event.preventDefault();
                $(this).parents('.zptReferenceField').find('.zptReferenceFieldPreview,.zptReferenceFieldStorage').val('');
            });

		    var sc = document.createElement('script');
		    sc.src = portal_url + '/referencebrowser.js';
		    sc.async = true;
		    document.body.appendChild(sc);
		    if (!window.referenceBrowserLoaded) {
		        window.referenceBrowserLoaded = true;
		    }

        
        });
    
    }
})(jQuery);
