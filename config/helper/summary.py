import json
import os

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_features(data, file_name, summary, module=None):
    if isinstance(data, dict):
        # Check if the current level contains 'features'
        if 'features' in data:
            features = data.get('features', {})
            acquisition = data.get('acquisition', {})
            node = data.get('node', {})
            table_data = {**acquisition, **node}
            core = features.get('core')
            mod_id = features.get('mod_id')
            mod_version = features.get('mod_version')

            combined_data = {**features, "table_data": table_data, "module": module}
            combined_data['file_name'] = file_name
            if core in summary:
                summary[core].append(combined_data)
            else:
                summary[core] = [combined_data]
        else:
            # Recursively check nested dictionaries
            for key, value in data.items():
                if isinstance(value, dict):
                    extract_features(value, file_name, summary, module=key)

def generate_summary(directory):
    summary = {'PTC': [], 'ADC': [], 'CVD': []}

    for file_name in os.listdir(directory):
        if not file_name.endswith('.json'):
            continue

        file_path = os.path.join(directory, file_name)
        data = load_json(file_path)
        extract_features(data, file_name, summary)

    return summary

def generate_nested_table_html(table_data):
    headers = []
    sub_headers = []
    values = []

    for key, value in table_data.items():
        if isinstance(value, dict):
            if 'min' in value and 'max' in value and 'default' in value:
                headers.append((key.replace('_', ' ').title(), 3))
                sub_headers.extend(['Min', 'Max', 'Default'])
                values.extend([value.get('min', 'N/A'), value.get('max', 'N/A'), value.get('default', 'N/A')])
            elif 'component_values' in value and 'default_index' in value:
                headers.append((key.replace('_', ' ').title(), 2))
                sub_headers.extend(['Component Values', 'Default Index'])
                values.extend([', '.join(map(str, value.get('component_values', []))), value.get('default_index', 'N/A')])
            elif 'min' in value and 'max' in value:
                headers.append((key.replace('_', ' ').title(), 2))
                sub_headers.extend(['Min', 'Max'])
                values.extend([value.get('min', 'N/A'), value.get('max', 'N/A')])
        else:
            headers.append((key.replace('_', ' ').title(), 1))
            sub_headers.append('')
            values.append(value)

    nested_table_html = "<table border='1'>"
    nested_table_html += "<tr>" + "".join([f"<th colspan='{colspan}'>{header}</th>" for header, colspan in headers]) + "</tr>"
    nested_table_html += "<tr>" + "".join([f"<th>{sub_header}</th>" for sub_header in sub_headers]) + "</tr>"
    nested_table_html += "<tr>" + "".join([f"<td>{value}</td>" for value in values]) + "</tr>"
    nested_table_html += "</table>"

    return nested_table_html

def generate_html_report(summary, output_file):
    html_content = """
    <html>
    <head>
        <title>Summary Report</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 15px;
                text-align: center;
            }
            tr:hover {
                background-color: #cccccc;
            }
            th {
                background-color: #f2f2f2;
                position: sticky;
                top: 0px;
            }
            .true {
                background-color: #c6efce;
            }
            .false {
                background-color: #ffc7ce;
            }
            tr:hover .true {
                background-color: #7cbf79;
            }
            .highlight {
                background-color: #ffeb3b;
            }
        </style>
        <script>
            function toggleDetails(rowId) {
                var detailsRow = document.getElementById('details-' + rowId);
                var deviceNameCell = document.getElementById('device-name-' + rowId);
                if (detailsRow.style.display === 'none') {
                    detailsRow.style.display = 'table-row';
                    deviceNameCell.classList.add('highlight');
                } else {
                    detailsRow.style.display = 'none';
                    deviceNameCell.classList.remove('highlight');
                }
            }
        </script>
    </head>
    <body>
        <h2>Summary Report</h2>
        <table>
            <tr>
                <th>Device Series</th>
                <th>Core with Version</th>
                <th>Self</th>
                <th>Mutual</th>
                <th>Scroller</th>
                <th>Surface</th>
                <th>Gesture</th>
                <th>Hardware Shield</th>
                <th>Timer Shield</th>
                <th>CSD</th>
                <th>PTC Prescaler</th>
                <th>Frequency Hop</th>
                <th>Frequency Hop Auto</th>
                <th>Low Power Software</th>
                <th>Low Power Event</th>
                <th>Lump Mode</th>
                <th>Boost Mode</th>
                <th>Wake Up</th>
                <th>Trust Zone</th>
                <th>X/Y Multiplex</th>
                <th>Unidirectional Tune</th>
                <th>Bidirectional Tune</th>
                <th>No-Standby</th>
            </tr>
    """

    row_id = 0
    for core in ['PTC', 'ADC', 'CVD']:
        for item in summary[core]:
            row_id += 1
            mod_info = f"<br/><i>{item.get('module')}</i>" if item.get('core') in ['PTC', 'ADC'] else ""
            html_content += f"""
            <tr onclick="toggleDetails({row_id})">
                <td id="device-name-{row_id}">{item.get('file_name').split(".")[0]}</td>
                <td>{item.get('core')} {mod_info}</td>
                <td class="{str(item.get('self')).lower()}">{item.get('self')}</td>
                <td class="{str(item.get('mutual')).lower()}">{item.get('mutual')}</td>
                <td class="{str(item.get('scroller')).lower()}">{item.get('scroller')}</td>
                <td class="{str(item.get('surface')).lower()}">{item.get('surface')}</td>
                <td class="{str(item.get('gesture')).lower()}">{item.get('gesture')}</td>
                <td class="{str(item.get('hardware_shield')).lower()}">{item.get('hardware_shield')}</td>
                <td class="{str(item.get('timer_shield')).lower()}">{item.get('timer_shield')}</td>
                <td class="{str(item.get('csd')).lower()}">{item.get('csd')}</td>
                <td class="{str(item.get('ptc_prescaler')).lower()}">{item.get('ptc_prescaler')}</td>
                <td class="{str(item.get('frequency_hop')).lower()}">{item.get('frequency_hop')}</td>
                <td class="{str(item.get('frequency_hop_auto')).lower()}">{item.get('frequency_hop_auto')}</td>
                <td class="{str(item.get('low_power_software')).lower()}">{item.get('low_power_software')}</td>
                <td class="{str(item.get('low_power_event')).lower()}">{item.get('low_power_event')}</td>
                <td class="{str(item.get('lump_mode')).lower()}">{item.get('lump_mode')}</td>
                <td class="{str(item.get('boost_mode')).lower()}">{item.get('boost_mode')}</td>
                <td class="{str(item.get('wake_up')).lower()}">{item.get('wake_up')}</td>
                <td class="{str(item.get('trust_zone')).lower()}">{item.get('trust_zone')}</td>
                <td class="{str(item.get('xy_multiplex')).lower()}">{item.get('xy_multiplex')}</td>
                <td class="{str(item.get('unidirectionalTune')).lower()}">{item.get('unidirectionalTune')}</td>
                <td class="{str(item.get('bidirectionalTune')).lower()}">{item.get('bidirectionalTune')}</td>
                <td class="{str(item.get('noStandbydevice')).lower()}">{item.get('noStandbydevice')}</td>
            </tr>
            <tr id="details-{row_id}" style="display:none;">
                <td colspan="20">
                    {generate_nested_table_html(item.get('table_data', {}))}
                </td>
            </tr>
            """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_file, 'w') as file:
        file.write(html_content)

def main():
    directory = '../json/'  # Update this to your directory path

    summary = generate_summary(directory)
    generate_html_report(summary, 'summary_output.html')

if __name__ == "__main__":
    main()
