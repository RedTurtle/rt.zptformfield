==============================================
This isn't the form library you're looking for
==============================================

95% you don't need this package: try some real Plone form libraries like:

* `z3c.form`__
* `collective.wtforms`__

__ http://pythonhosted.org/z3c.form/
__ https://github.com/collective/collective.wtforms

Move along... move along...

=========================================
Your mind powers will not work on me, boy
=========================================

If you really want to know what is this, keep reading.

.. contents::
   :local:

Introduction
============

**This is not a form library** for Plone, it's only a set of **ZPT macros** that you can use to 
create HTML form in the old way, keeping the Plone layout.
For this reason this product will not handle what to do when you submit the form, it's only focused onto
rendering some advanced fields.

The nice thing is that you can use those macros with the old-way-TTW approach.

Field reference
===============

Every field has some custom options you can/must configure, but some of them are globals:

``fieldName`` (mandatory)
    The name of the field, that is the name you will read from the request when sending the form 
``fieldLabel``
    The label of the field
``fieldHelp``
    Additional explanation of the field
``required``
    Display the required UI information of the field. **Please note** that it's only a visual effect,
    you are in charge of really handle the requirement.
``cssFieldAdditionalClasses``
    Additional CSS classes that will be appended to the div containing the whole field

Lines Field
-----------

This field can be used to provide a list of elements (strings) for the submitted form.
Elements are loaded one at time from a text input.

.. image:: http://blog.redturtle.it/pypi-images/rt.zptformfield/rt.zptformfield-0.1.0-lines01.png
   :alt: Lines field
   :align: center

The field name will be composed as "*fieldName*:list", so you will read a list of element directly from the request.

Additional parameters
~~~~~~~~~~~~~~~~~~~~~

``fieldType`` (default to "text")
    The type of the HTML input field used to populate the list. You can change it to
    HTML 5 new elements type to use some of the browser native features.
``pattern``
    The HTML 5 pattern attribute, for field validation. This regex is used to validate the field value before
    adding it to the list
``elements``
    Existings elements to be used to populate the list. Provide a sequence of dicts with a "title" and "value"
    couple

How to use
~~~~~~~~~~

Call the macro

.. code-block:: xml

    <tal:field define="fieldName string:test_lines_field;
                       fieldLabel string:Testing lines field;
                       fieldHelp string:Write something, then add it;
                       ">
        <metal:field-content use-macro="context/@@rt.zptformfield.lines/field" />
    </tal:field>

You need to include a JavaScript in your final HTML.

.. code-block:: xml

    <metal:head fill-slot="javascript_head_slot">
        <metal:field-content use-macro="context/@@rt.zptformfield.lines/javascript_helpers" />
    </metal:head>

Autocomplete Lines Field
------------------------

This field can be used to provide a list of elements (strings) for the submitted form.
Elements are selected by an autocomplete feature obtained through `jQueryUI Autocomplete`__;
in Plone the easyest way to get this is by installing `collective.js.jqueryui`__.

__ http://jqueryui.com/autocomplete/
__ http://pypi.python.org/pypi/collective.js.jqueryui

.. image:: http://blog.redturtle.it/pypi-images/rt.zptformfield/rt.zptformfield-0.1.0-autocomplete01.png
   :alt: Autocomplete lines field
   :align: center

The field name will be composed as "*fieldName*:list", so you will read a list of element directly from the request.

Additional parameters
~~~~~~~~~~~~~~~~~~~~~

``source`` (mandatory)
    An URL that jQueryUI will call for getting selectable elements. This call must return a valid JSON sequence with
    "value" and "label" elements.
``elements``
    Existings elements to be used to populate the list. Provide a sequence of dicts with a "title" and "value"
    couple

How to use
~~~~~~~~~~

Call the macro

.. code-block:: xml

    <tal:field define="fieldName string:test_lines_field;
                       source string:${portal_url}/@@rt.zptformfield.test.vocab;
                       fieldLabel string:Testing autocomplete field;
                       fieldHelp string:Write something and test the autocomplete feature;
                       ">
        <metal:field-content use-macro="context/@@rt.zptformfield.autocomplete_lines/field" />
    </tal:field>

You need to include a JavaScript in your final HTML.

.. code-block:: xml

    <metal:head fill-slot="javascript_head_slot">
        <metal:field-content use-macro="context/@@rt.zptformfield.autocomplete_lines/javascript_helpers" />
    </metal:head>

TinyMCE Field
-------------

This field render a textarea and trigger the default Plone WYSIWYG editor on the field (using the Products.TinyMCE features,
version 1.3 or better).

.. image:: http://blog.redturtle.it/pypi-images/rt.zptformfield/rt.zptformfield-0.1.0-tinymce01.png
   :alt: TinyMCE field
   :align: center

Additional parameters
~~~~~~~~~~~~~~~~~~~~~

``rows``
    Number of rows of the textarea
``cols``
    Number of columns of the textarea
``configuration_method``
    The view to be called for obtaining TinyMCE configuration. Do not use for loading the default ones
``configuration_json``
    Directly provide the JSON configuration. Do not use to load it from the "*configuration_method*"
``value``
    Default text in the field

How to use
~~~~~~~~~~

Call the macro

.. code-block:: xml

    <tal:field define="fieldName string:test_lines_field;
                       fieldLabel string:Testing TinyMCE field;
                       fieldHelp string:You can use the WYSIWYG editor below;
                       rows python:15;
                       value string:The cat is on the table;
                       ">
        <metal:field-content use-macro="context/@@rt.zptformfield.tinymce/field" />
    </tal:field>

Reference Field
---------------

This field render a selection of a site content using the native `archetypes.referencebrowserwidget`__
machinery. The only problem is that the AJAX call **must** be called on a real Archetypes content that
provide a (not multivalued) reference field of a well know name (even if hidden and never used).

__ https://pypi.python.org/pypi/archetypes.referencebrowserwidget/

.. image:: http://blog.redturtle.it/pypi-images/rt.zptformfield/rt.zptformfield-0.1.0-reference01.png
   :alt: Reference field
   :align: center

The submitted data will be the uuid of the selected document.

Additional parameters
~~~~~~~~~~~~~~~~~~~~~

``startup_directory``
    The directory where start browsing the site. Default is the current context.
``context_helper``
    The context of which call the ``refbrowserhelper`` view. Default is the current context.
``fake_field_name`` (mandatory)
    This field name will not be used in the form, but must be an existing Archetypes reference field name
    on the context defined by "context_helper".
``search_index``
    The TextIndex to be used for the overlay search box. Default is Plone default "SearchableText".

How to use
~~~~~~~~~~

Call the macro

.. code-block:: xml

    <tal:field define="fieldName string:test_reference_field;
                       fake_field_name string:foo_field;
                       fieldLabel string:Testing reference browser field;
                       fieldHelp string:Use the Plone reference browser feature.
                       ">
        <metal:field-content use-macro="context/@@rt.zptformfield.reference/field" />
    </tal:field>

In the example above we didn't provide ``context_helper`` parameter so it *must* be called on a Plone content
that behave the "foo_field" singlevalued reference field.

You need to include a JavaScript in your final HTML.

.. code-block:: xml

    <metal:head fill-slot="javascript_head_slot">
        <metal:field-content use-macro="context/@@rt.zptformfield.reference/javascript_helpers" />
    </metal:head>

Multivalued Reference Field
---------------------------

This is the same as the reference field above, but from the overlay displayed you will be able to select multiple
elements.

.. image:: http://blog.redturtle.it/pypi-images/rt.zptformfield/rt.zptformfield-0.1.0-multireference01.png
   :alt: Reference field
   :align: center

The submitted data will be the a uuid list of selected documents.

Additional parameters
~~~~~~~~~~~~~~~~~~~~~

See "Reference Field"

How to use
~~~~~~~~~~

Call the macro

.. code-block:: xml

    <tal:field define="fieldName string:test_multivalued_reference_field;
                       fake_field_name string:relatedItems;
                       fieldLabel string:Testing multivalued reference browser field;
                       fieldHelp string:Use the Plone reference browser feature.
                       ">
        <metal:field-content use-macro="context/@@rt.zptformfield.multivalued_reference/field" />
    </tal:field>

In the example above we didn't provide ``context_helper`` parameter so it *must* be called on a Plone content
that behave the "relatedItems" multivalued reference field (by default: all content types).

You need to include a JavaScript in your final HTML.

.. code-block:: xml

    <metal:head fill-slot="javascript_head_slot">
        <metal:field-content use-macro="context/@@rt.zptformfield.multivalued_reference/javascript_helpers" />
    </metal:head>

Calendar Field
--------------

This field can be used to submit a date (or date-time) using the Plone default calendar.
Date can be filled by using a set of HTML select elements or with a popup calendar widget.

.. image:: http://blog.redturtle.it/pypi-images/rt.zptformfield/rt.zptformfield-0.2.0-calendar01.png
   :alt: Calendar field
   :align: center

This field is based on Plone inner calendar support (JavaScript and ZPT macros) so you can't use this outside
Plone.

Additional parameters
~~~~~~~~~~~~~~~~~~~~~

``value``
    The date to be displayed (a `Zope DateTime`__ object). Default will not show any date.
``show_hm``
    Boolean value for showing the hours/minutes widget elements. Default will show them.
``show_ymd``
    Boolean value for showing the day widget elements. Default will show them.
``starting_year``
    Integer value for defining the first year to be used in the year combo box.
``ending_year``
    Integer value for defining the last year to be used in the year combo box.
``future_years``
    Integer value for defining how many years in the future (from current date) will be shown
    in the calendar widget. Will be ignored if ``ending_year`` is provided.  
``minute_step``
    If minutes combobox is shown, define the interval between minutes values. Plone default is 5.
``calendar_lang``
    Language of the calendar popup UI. For an old and never fixed `Plone bug`__ the default is to
    english language and not to the current language.
    Change at your own risk. Also: *note* that this parameter is for the ``javascript_helpers``
    macros (see example below)

__ https://pypi.python.org/pypi/DateTime
__ https://dev.plone.org/ticket/13189


How to use
~~~~~~~~~~

Call the macro

.. code-block:: xml

    <tal:field define="fieldName string:test_calendar_field;
                       fieldLabel string:Testing Calendar field;
                       fieldHelp string:The standard Plone calendar;">
        <metal:field-content use-macro="context/@@rt.zptformfield.calendar/field" />
    </tal:field>

You need to include a JavaScript in your final HTML. Another **warning** about the usage of
``calendar_lang`` parameter: it's buggy.

.. code-block:: xml

    <metal:head fill-slot="javascript_head_slot" tal:define="calendar_lang context/@@plone_portal_state/language;">
        <metal:field-content use-macro="context/@@rt.zptformfield.calendar/javascript_helpers" />
    </metal:head>

Finally, the calendar popup needs some CSS styles:

.. code-block:: xml

    <metal:head fill-slot="style_slot">
        <link rel="stylesheet" type="text/css" href="jscalendar/calendar-system.css"
              tal:attributes="href string:$portal_url/jscalendar/calendar-system.css" />
    </metal:head>

Live examples
=============

This product contains a set of demo views for all fields. You must activate them by including the ``tests.zcml``
file.

::

    [instance]
    eggs +=
        ...
        rt.zptformfield
    
    zcml +=
        ...
        rt.zptformfield:tests.zcml

Check `the code`__ for an updated list of examples.

__ https://github.com/RedTurtle/rt.zptformfield/blob/master/src/rt/zptformfield/tests/configure.zcml

=======
Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
