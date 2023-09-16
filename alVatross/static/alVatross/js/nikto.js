function CreateNiktoCommand() {
    var target_url_value = get_target_url();
    var port_num = get_port_number();
    var path = get_path();
    var use_ssl = get_use_ssl();
    var sleep = get_sleep();
    var use_proxy = get_use_proxy();

    var output_file_format = get_output_file_format()
    file_format = select_file_format(output_file_format.value)
    file_extention = select_file_extention(output_file_format.value) 
    var output_filename = get_output_filename()
    var result = create_nikto_command(target_url_value, port_num, use_ssl, path, sleep, use_proxy, output_filename, file_extention, file_format)
    result_element = get_result()
    result_element.value = result
};

function get_target_url(){
    target_url = document.getElementById("target_url");
    return target_url.value;
}

function get_port_number(){
    port_number = document.getElementById("port_number");
    return port_number.value;
}

function get_path(){
    path = document.getElementById("path");
    return path.value;
}

function get_use_ssl() {
    use_ssl_elements = document.getElementsByName("use_ssl");
    use_ssl = select_use_ssl_value(use_ssl_elements);
    return use_ssl;
}

function get_use_proxy() {
    var use_proxy_element = document.getElementsByName("use_proxy");
    use_proxy_elements.forEach(function(e){
        if (e.checked && e.value == "ON"){
            return '-useproxy';
        }
    })
    return '';
}

function get_sleep() {
    sleep = document.getElementById("sleep")
    return sleep.value
}

function get_output_file_format() {
    return document.getElementById("output_file_format")
}

function get_output_filename() {
    return document.getElementById("output_filename")
}

function get_result() {
    return document.getElementById("result")
}

function create_nikto_command(target_url, port_num, use_ssl, path, sleep, use_proxy, output_filename, file_extention, file_format) {
    return "perl nikto.pl -host " + target_url + " -p "+ port_num + " " + use_ssl + " -root " + path + " -sleep " + sleep + " " + use_proxy + " -o "  + output_filename.value + file_extention + " -Format "+ file_format
}

function select_file_format(file_format){
    switch (file_format){
        case 'text':
            return 'txt';
        case 'csv':
            return 'csv';
        case 'json':
            return 'json';
        case 'htm':
            return 'htm';
        case 'nbe':
            return 'nbe';
        case 'sql':
            return 'sql';
        case 'xml':
            return 'xml';
    }
}

function select_file_extention(file_format){
    switch (file_format){
        case 'text':
            return '.txt';
        case 'csv':
            return '.csv';
        case 'json':
            return '.json';
        case 'htm':
            return '.html';
        case 'nbe':
            return '.nbe';
        case 'sql':
            return '.sql';
        case 'xml':
            return '.xml';
    }
}

["target_url", "port_number", "path", "sleep", "output_file_format", "output_filename"].forEach(function(e){
    document.getElementById(e).addEventListener('change', CreateNiktoCommand);
}


//document.getElementById("target_url").addEventListener('change', CreateNiktoCommand);
//document.getElementById("port_number").addEventListener('change', CreateNiktoCommand);
//document.getElementById("path").addEventListener('change', CreateNiktoCommand);
//document.getElementById("sleep").addEventListener('change', CreateNiktoCommand);

document.getElementsByName("use_proxy").forEach(function(e){
    e.addEventListener('change', CreateNiktoCommand);
});
var radio_button_use_ssl  = get_use_ssl();
radio_button_use_ssl.forEach(function(e){
    e.addEventListener('change', CreateNiktoCommand);
});
//document.getElementById("output_file_format").addEventListener('change', CreateNiktoCommand)
//document.getElementById("output_filename").addEventListener('change', CreateNiktoCommand)
