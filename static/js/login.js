$("#btn").click(function login() {
    var username = $("#un").val();
    var password = $("#pw").val();
    if (username === '') {
        alert("工号不能为空");
        return false;
    } else if (password === '') {
        alert("密码不能为空");
        return false;
    }
    var data = {username: username, password: password};
    $.ajax({
        type: 'post',
        url: "/login_commit",
        data: data,
        dataType: 'json',
        success: function (msg) {
            console.log(msg);
            if (msg['message'] === 1) {
                window.location.href = "/";
            } else if (msg['message'] === 2) {
                alert("工号或密码错误，重置密码请联系管理员");
            } else if (msg['message'] === 3) {
                alert("工号不存在，查询工号请联系管理员");
            } else {
                alert("登陆失败，请重试");
            }
        }
    });
});
