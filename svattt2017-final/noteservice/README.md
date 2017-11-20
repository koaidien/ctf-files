<h1>Note Service</h1>

Không rõ tại sao mình làm bài này bằng formatstring thì không chạy, thôi mình liều dùng cách heap và vẫn ăn được thật. Ý tưởng thì đơn giản thôi, mình thấy chương trình chạy thế này:
    <p>- Ban đầu nạp vào flag và để ở note có index là 0.</p>
    <p>- Phần tạo ra 1 note và cả phần đã nạp vào chương trình đều malloc 2 lần: 1 lần malloc đúng 0x10 bytes, lần còn lại malloc bằng size của của mình nhập vào.</p>
    <p>- Hàm delete thì xóa 2 vùng, vùng thứ 2 là vùng data và không xóa data đó.</p>
Đây là cách mình dùng:
    <p>- Nhập 32 kí tự ở chỗ hàm login để biến isNormal chuyển về 1 (trong hàm Login cố ý làm thế).</p>
    <p>- delete index 0.</p>
    <p>- Tạo note mới với size mình đoán được, vì mình không biết chính xác vùng này sẽ đặt vào fastbin nào nên mình thử với các độ dài khác nhau, cách nhau 0x10 bytes mỗi lần thử và quan trọng nhất là không protect.</p>
    <p>- Show flag thôi, flag bây giờ nằm ở index 0.</p>
