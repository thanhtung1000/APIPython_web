
Trong bài làm này, em xây dựng một hệ thống quản lý sinh viên đơn giản, phục vụ cho việc lưu trữ và xử lý thông tin sinh viên trong một lớp học hoặc một cơ sở đào tạo. Hệ thống cho phép người dùng thực hiện các chức năng cơ bản như thêm sinh viên mới, chỉnh sửa thông tin, xóa sinh viên, và hiển thị danh sách sinh viên đã nhập. Ngoài ra, người dùng cũng có thể tìm kiếm sinh viên theo mã để tra cứu nhanh chóng.

Để triển khai hệ thống, em sử dụng ngôn ngữ lập trình Python kết hợp với framework FastAPI để xây dựng phần backend. FastAPI là một công cụ hiện đại, nhẹ và rất phù hợp cho việc phát triển các API RESTful. Phần giao diện người dùng được xây dựng bằng HTML, CSS và JavaScript, với thiết kế đơn giản, dễ sử dụng và hỗ trợ đầy đủ tiếng Việt. Để đảm bảo hiển thị tiếng Việt không bị lỗi dấu, em sử dụng font chữ Noto Sans từ Google Fonts và cấu hình mã hóa UTF-8 trong toàn bộ hệ thống.

Về phần lưu trữ dữ liệu, hệ thống sử dụng cơ sở dữ liệu Microsoft SQL Server. Các bảng dữ liệu được thiết kế với kiểu dữ liệu `NVARCHAR` để đảm bảo khả năng lưu trữ tiếng Việt có dấu. Việc kết nối giữa Python và SQL Server được thực hiện thông qua thư viện SQLAlchemy, giúp ánh xạ các bảng dữ liệu thành các lớp Python một cách thuận tiện và rõ ràng.

Giao diện web của hệ thống bao gồm một biểu mẫu nhập liệu cho phép người dùng điền thông tin sinh viên như họ tên, lớp, giới tính, ngày sinh, số điện thoại và mã sinh viên. Dữ liệu sau khi nhập sẽ được gửi lên server thông qua Fetch API và lưu vào cơ sở dữ liệu. Bên dưới biểu mẫu là bảng danh sách sinh viên, hiển thị toàn bộ dữ liệu đã nhập. Mỗi dòng trong bảng đều có nút “Sửa” và “Xóa” để người dùng thao tác trực tiếp.

Ngoài ra, hệ thống còn cung cấp giao diện Swagger UI tại địa chỉ `http://localhost:8000/docs`, cho phép người dùng hoặc lập trình viên kiểm thử các API một cách trực quan. Hệ thống cũng được cấu hình để có thể chia sẻ API cho các thiết bị khác trong cùng mạng nội bộ, giúp việc sử dụng trở nên linh hoạt và tiện lợi hơn.

Qua bài làm này, em đã hiểu rõ hơn về cách xây dựng một hệ thống web đơn giản, cách thiết kế API, xử lý dữ liệu Unicode, và kết nối với cơ sở dữ liệu thực tế. Đây là nền tảng quan trọng để phát triển các ứng dụng lớn hơn trong tương lai.
<img width="1849" height="579" alt="image" src="https://github.com/user-attachments/assets/57d9be88-bde9-480c-97cd-ea7dfaba4c6d" />
