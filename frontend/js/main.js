$(document).ready(function(){

    console.log("hello")
    //获取http://127.0.0.1/api/surveys/返回的json数据
    var url = "http://127.0.0.1/api/surveys/"
    $.getJSON(url,function(resp){
        console.log(resp.surveys)
        // for survey in resp.surveys
        $.each(resp.surveys,function(i,survey){
            console.log(survey.name)
            $("body").html("<h1>" + survey.name  + "</h1>")

            // 添加section
            var section_survey = document.createElement("section")
            section_survey.setAttribute("class","survey")
            section_survey.setAttribute("value",survey.id)
            $("body").append(section_survey)
            //在 section_survey中添加 问题
            console.log(survey.questions)
            // 遍历 questions
            $.each(survey.questions,function(i,question){
                var header_question = document.createElement("header")
                header_question.setAttribute("class","question")
                header_question.innerText = question.text
                section_survey.append(header_question)
                //在 问题中添加选项


            });

            
        })
        // 添加一个标题
    

    });

});