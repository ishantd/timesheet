// console.log("HELLo")
var weekString;
var y;
var w;
$('#ts_form').submit(function(e){
    e.preventDefault();
    var myform = $("form");
    var disabled = myform.find(':input:disabled').removeAttr('disabled'); // Ser array only takes enabled fields, this is why
    var data = myform.serializeArray();
    console.log(data);
    disabled.attr('disabled','disabled');
    var employee_id = $('#emp_id').text();
    var dept = $("#emp_dep").text();
    weekString = $("#week").val();
    y = parseInt(weekString.substring(0, 4));
    w = parseInt(weekString.replace(year.toString()+'-W', ''));
    hour_sum = (hours) => {
        var sum=0;
        for (var i=0 ; i<hours.length; i++) {
            sum = hours[i] + sum;
        }
        return sum;
    };
    // console.log(data)
    employee_id = parseInt(employee_id.replace('ID: ', ''))
    var ReportData = [];
    for (var i = 0; i < (data.length+1)/9; i++) {
        var dataObject = {};
        var p_id;
        var activity;
        var hours = [];
        for (var j = i * 9; j < (i+1)*9 ; j++) {
           if(data[j] != undefined) {
            if((j==0 || j%9==0) && data[j].name == "project") {
                if (data[j].value == "Holiday/Leave") {
                    p_id = 0;
                }
                else {
                    p_id = parseInt(data[j].value);
                }
            }
            if(data[j].name == "activity"){
                activity = data[j].value;
            }
            if (j > (i*9)+1 && data[j].name.includes("hours")) {
                hours.push(parseInt(data[j].value)) ;
            }
        }
        }
        if (hours.length == 7) {
            dataObject = {
                employee: employee_id,
                project: p_id,
                activity: activity,
                department_name: dept,
                everyday_hours: hours.join(),
                hours_reported: hour_sum(hours),
                week : w,
                year : y
            };
        }
        
        ReportData.push(dataObject);
    }
    // console.log(ReportData)
    ReportData.pop();
    
    // for (var i=0; i<ReportData.length; i++){
    //     $.post("/timesheetEntry/", ReportData[i], function(){
    //         console.log("Data successfully sent");
    //     });
    // }
    
    return false;
});