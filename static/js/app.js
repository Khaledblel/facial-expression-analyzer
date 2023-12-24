function analyzeExpression() {
    var formData = new FormData($('#uploadForm')[0]);
  
    $.ajax({
        url: '/predict',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (response) {
            $('#result').html('Predicted Emotion: ' + response.predicted_emotion);
            var uploadedImage = $('#uploadedImage');
            uploadedImage.attr('src', URL.createObjectURL($('#imageInput')[0].files[0]));
            uploadedImage.show();
        },
        error: function (error) {
            console.log(error);
        }
    });
  }
  