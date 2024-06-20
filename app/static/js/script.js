//document.addEventListener('DOMContentLoaded', function () {
//    const modelChoice = document.getElementById('model_choice');
//    const geminiOption = document.getElementById('gemini_option');
//
//    modelChoice.addEventListener('change', function () {
//        if (modelChoice.value === 'google-gemini') {
//            geminiOption.disabled = false;
//        } else {
//            geminiOption.disabled = true;
//            geminiOption.value = 'professional';
//        }
//    });
//});

document.addEventListener('DOMContentLoaded', function () {
    const modelChoice = document.getElementById('model_choice');
    const geminiOption = document.getElementById('gemini_option');

    modelChoice.addEventListener('change', function () {
        if (modelChoice.value === 'google-gemini') {
            geminiOption.querySelectorAll('option').forEach(option => {
                option.style.display = 'block';  // Show all options
            });
        } else if (modelChoice.value === 't5-pubmed') {
            geminiOption.querySelectorAll('option').forEach(option => {
                if (option.value === 'professional') {
                    option.style.display = 'block';  // Show 'Professional' option
                } else {
                    option.style.display = 'none';   // Hide other options
                }
            });
            geminiOption.value = 'professional';  // Select 'Professional' by default
        } else {
            geminiOption.value = 'professional';  // Select 'Professional' by default for other models
        }
    });

    // Initial setup based on current value of modelChoice
    if (modelChoice.value === 'google-gemini') {
        geminiOption.querySelectorAll('option').forEach(option => {
            option.style.display = 'block';  // Show all options
        });
    } else if (modelChoice.value === 't5-pubmed') {
        geminiOption.querySelectorAll('option').forEach(option => {
            if (option.value === 'professional') {
                option.style.display = 'block';  // Show 'Professional' option
            } else {
                option.style.display = 'none';   // Hide other options
            }
        });
        geminiOption.value = 'professional';  // Select 'Professional' by default
    } else {
        geminiOption.value = 'professional';  // Select 'Professional' by default for other models
    }
});


