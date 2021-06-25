$("#btn").click(function login() {
    var math = Number($("#math").val());
    var english = Number($("#english").val());
    var specialty = Number($("#specialty").val());
    var politics = Number($("#politics").val());
    var vocabulary = Number($("#vocabulary").val());
    var spoken = Number($("#spoken").val());
    var hearing = Number($("#hearing").val());
    var remarks = $("#remarks").val();
    if (math === '') {
        math = 0;
    }
    if (english === '') {
        english = 0;
    }
    if (specialty === '') {
        specialty = 0;
    }
    if (politics === '') {
        politics = 0;
    }
    if (vocabulary === '') {
        vocabulary = 0;
    }
    if (spoken === '') {
        spoken = 0;
    }
    if (hearing === '') {
        hearing = 0;
    }
    if(!isNumber(math)) {
        alert('数学不是有效的数字');
        return false;
    }else if(!isNumber(english)) {
        alert('英语不是有效的数字');
        return false;
    }else if(!isNumber(specialty)) {
        alert('专业课不是有效的数字');
        return false;
    }else if(!isNumber(politics)) {
        alert('政治不是有效的数字');
        return false;
    }else if(!isNumber(vocabulary)) {
        alert('词汇不是有效的数字');
        return false;
    }else if(!isNumber(spoken)) {
        alert('口语不是有效的数字');
        return false;
    }else if(!isNumber(hearing)) {
        alert('听力不是有效的数字');
        return false;
    }
    var data = {math:math, english:english, specialty:specialty, politics:politics, vocabulary:vocabulary, spoken:spoken, hearing:hearing, remarks:remarks};
    $.ajax({
        type: 'post',
        url: "/submit_commit",
        data: data,
        dataType: 'json',
        success: function (msg) {
            console.log(msg);
            if (msg['message'] === 1) {
                window.location.href = "/";
            } else {
                alert("数据库写入失败，请重试");
            }
        }
    });
});

// 验证是否为数字
function isNumber(value)
{
    return typeof value === 'number' && !isNaN(value);
}
