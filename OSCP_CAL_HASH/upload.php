<!DOCTYPE html>
<html>

<body>

<div align="center">
<form action="" method="post" enctype="multipart/form-data">
    <br>
    <b>Select image : </b> 

    <!-- 文件上传框，name="file" 表示后端通过 $_FILES["file"] 取到这个文件 -->
    <input type="file" name="file" id="file" style="border: solid;">

    <!-- 提交按钮，name="submit" 方便后端判断是否点击了提交 -->
    <input type="submit" value="Submit" name="submit">
</form>
</div>

<?php

// 如果用户点击了提交按钮，就进入上传处理逻辑
if(isset($_POST["submit"])) {

    // 随机生成 1 到 100 的数字
    // 后面会参与文件名哈希，避免文件名完全固定
	$rand_number = rand(1,100);

    // 上传目录
	$target_dir = "uploads/";

    // 目标文件名：
    // basename($_FILES["file"]["name"]) 取上传文件原始名字，例如 a.png
    // 然后拼接随机数，再做 md5
    // 最终结果类似 uploads/5d41402abc4b2a76b9719d911017c592
	// .代表拼接
	$target_file = $target_dir . md5(basename($_FILES["file"]["name"].$rand_number));

    // 这个变量保存“原始文件名”的路径，例如 uploads/a.png
    // 主要是后面拿来提取扩展名
	$file_name = $target_dir . basename($_FILES["file"]["name"]);

    // 默认允许上传
	$uploadOk = 1;

    // 取文件扩展名，并转成小写
    // 例如 a.PNG -> png
	$imageFileType = strtolower(pathinfo($file_name,PATHINFO_EXTENSION));

    // 获取浏览器上报的 MIME 类型
    // 例如 image/png
    // 但这个值通常不够可靠，因为客户端可以伪造
	$type = $_FILES["file"]["type"];

    // getimagesize() 会尝试读取上传文件的图片信息
    // 如果真的是图片，通常能返回宽高、mime 等信息
    // 如果不是有效图片，可能返回 false
	$check = getimagesize($_FILES["file"]["tmp_name"]);

    // 只允许 mime 为 image/png 或 image/gif 的文件通过
	if($check["mime"] == "image/png" || $check["mime"] == "image/gif"){
		$uploadOk = 1;
	}else{
		$uploadOk = 0;
		echo ":)";
	}

    // 如果检查通过，则移动上传文件到目标目录
    // 文件名会变成 md5值 + 原始扩展名
    // 例如 uploads/abcd1234efgh5678.png
    // 然后输出提示信息
    // 注意：这里只显示 /uploads/?，并没有把真实文件名直接打印出来
    // 说明作者可能不想让用户直接知道上传后的最终路径
  if($uploadOk == 1){
      move_uploaded_file($_FILES["file"]["tmp_name"], $target_file.".".$imageFileType);
      echo "File uploaded /uploads/?";
  }
}
?>

</body>
</html>