(function (a) {if (typeof define === "function" && define.amd) {define(["jquery", "jquery.validate"], a)} else {if (typeof module === "object" && module.exports) {module.exports = a(require("jquery"))} else {a(jQuery)}}
}(function (a) {
    a.extend(a.validator.messages, {
        required: "Это поле необходимо заполнить",
        remote: "Пожалуйста, введите правильное значение",
        email: "Пожалуйста, введите корректный адрес электронной почты",
        url: "Пожалуйста, введите корректный URL",
        date: "Пожалуйста, введите корректную дату",
        dateISO: "Пожалуйста, введите корректную дату в формате ISO",
        number: "Пожалуйста, введите число",
        digits: "Пожалуйста, вводите только цифры",
        chars: "Пожалуйста, вводите только буквы",
        creditcard: "Пожалуйста, введите правильный номер кредитной карты",
        equalTo: "Пожалуйста, введите такое же значение ещё раз",
        extension: "Пожалуйста, выберите файл с правильным расширением.",
        time: "Пожалуйста, введите корректное время с 00:00 до 23:59",
        maxlength: a.validator.format("Пожалуйста, введите не больше {0} символов"),
        minlength: a.validator.format("Пожалуйста, введите не меньше {0} символов"),
        rangelength: a.validator.format("Пожалуйста, введите значение длиной от {0} до {1} символов"),
        range: a.validator.format("Пожалуйста, введите число от {0} до {1}"),
        max: a.validator.format("Пожалуйста, введите число, меньшее или равное {0}"),
        min: a.validator.format("Пожалуйста, введите число, большее или равное {0}")
    });
    return a
}));
