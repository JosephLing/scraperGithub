{% block output_group -%}
{%- if cell.metadata.hide_output or nb.metadata.hide_input -%}
{%- else -%}
    {{ super() }}
{%- endif -%}
{% endblock output_group %}