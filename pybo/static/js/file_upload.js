var submit = document.getElementById('submitButton');
submit.onclick = showImage;

function showImage() {
    var newImage = document.getElementById('image-show').lastElementChild;
    newImage.style.visibility = "visible";

    document.getElementById('uploadLabel').style.display = 'none'; // "Upload Image" 라벨 숨기기

    document.getElementById('fileName').textContent = null; // 기존 파일 이름 지우기
}


function loadFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        var box1 = document.getElementById('box1');

        reader.onload = function (e) {
            var image = new Image();
            image.src = e.target.result;
            image.style.width = '100%'; // 이미지를 box1 너비에 맞게 조절
            image.style.height = '400px'; // 이미지를 box1 높이에 맞게 조절
            image.style.borderBottomLeftRadius= '10px';
            image.style.borderBottomRightRadius= '10px';


            // 기존 이미지가 있으면 삭제
            var existingImage = box1.querySelector('img');
            if (existingImage) {
                box1.removeChild(existingImage);
            }

            box1.appendChild(image);
            box1.style.visibility = 'visible'; // box1 표시
            showImage();
        };

        reader.readAsDataURL(input.files[0]);
    }
}

// 이미지가 업로드되면 Submit 버튼 클릭 없이 이미지를 바로 표시
document.getElementById('chooseFile').onchange = function () {
    loadFile(this);
    showImage();
};






