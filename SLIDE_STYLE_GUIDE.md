> **Ghi chú chuyển thể (07/2026):** Tài liệu gốc được soạn cho môn **Học máy** (cùng giảng viên); bản này dùng cho môn **Lập trình xử lý dữ liệu (UET.DSE2049)**. Toàn bộ nội dung phía dưới giữ nguyên văn — khi áp dụng cho môn này, thay các điểm sau:
>
> - **Thời lượng:** một buổi lý thuyết của môn này là 2 tiết ≈ **100 phút** → vùng an toàn là **30–40 slide thực dạy** (thay cho 120–130 phút / 35–45 slide trong guide).
> - **Đối tượng:** sinh viên năm 1–2 đã qua *Tư duy tính toán* (COM1050); môn này **thiên thực hành** — mọi khái niệm nên gắn với thao tác trên dữ liệu thật, ưu tiên demo/code hơn công thức.
> - **Ví dụ trong guide** (bagging, boosting, dendrogram…) là từ môn Học máy — chỉ minh hoạ *phong cách viết*, không phải nội dung môn này.
> - **Thuật ngữ cho môn này.** Thường **giữ tiếng Anh**: DataFrame, Series, index, dtype, groupby, merge/join, broadcasting, pipeline, regex, missing value, outlier, prompt, token, API. Thường **Việt hoá**: đọc/ghi file, làm sạch dữ liệu, trùng lặp, giá trị thiếu, biểu đồ đường/cột/phân tán, gộp nhóm. Lần đầu xuất hiện thuật ngữ giữ tiếng Anh, chú thích nghĩa tiếng Việt trong ngoặc. Trong code luôn dùng tên API nguyên bản.
> - **Slide code:** quy tắc "một ý chính" áp dụng cả cho code — mỗi slide một đoạn code ngắn làm trung tâm (≤ ~12 dòng), kèm output; không nhồi hai khối code độc lập vào một slide.

---

# Slide Style Guide

## How to use this guide

Không cần đọc toàn bộ tài liệu này mỗi lần sửa slide.

### Khi tạo một deck mới

Đọc theo thứ tự:
- `Mục tiêu sư phạm`
- `Nguyên tắc không thương lượng`
- `Cấu trúc chuẩn của một deck 120-130 phút`
- `Quy trình chuẩn khi tạo hoặc sửa slide`

### Khi review một deck cũ

Đọc theo thứ tự:
- `Rubric rà soát một lecture`
- `Tiêu chuẩn ở mức section`
- `Tiêu chuẩn ở mức slide`
- `Quy tắc về hình ảnh`
- `Quy tắc về wording`

### Khi review một slide cụ thể

Chỉ cần hỏi nhanh 4 câu:
- Slide này có đúng **một ý chính** không?
- Hình / công thức / bullet nào là **trung tâm**?
- Có thể bỏ bớt **20-30% chữ** mà vẫn giữ ý không?
- Caption và hình có đang nói **cùng một điều** không?

Nếu bất kỳ câu nào trả lời là `không`, nên sửa slide trước khi sửa câu chữ chi tiết.

## Phạm vi

Tài liệu này quy định tiêu chuẩn thiết kế và rà soát slide cho môn **Học máy** tại **Viện Trí tuệ nhân tạo, Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội**.

Phạm vi áp dụng:
- deck giảng lý thuyết 120-130 phút
- slide dùng để giảng trực tiếp trên lớp
- deck viết bằng HTML / Reveal.js

Tài liệu này **không** tối ưu trước cho:
- tutorial thực hành
- bài tập về nhà
- seminar nghiên cứu

## Mục tiêu sư phạm

Thứ tự ưu tiên:

1. **Dễ dạy trên lớp**
2. **Bám đúng logic kiến thức chuẩn**
3. **Dễ cho sinh viên tự đọc lại**

Hệ quả:
- slide không phải là giáo trình thu nhỏ
- slide phục vụ nhịp giảng, không cố ghi lại mọi điều giảng viên sẽ nói
- nếu phải chọn giữa “đầy đủ” và “dễ dạy”, ưu tiên “dễ dạy”

## Đối tượng người học

Đối tượng chuẩn:
- sinh viên năm 1-2
- nền toán tương đối ổn
- đã học đại số, giải tích
- lập trình ở mức ổn
- thiên lý thuyết hơn thiên ứng dụng

Hệ quả:
- có thể dùng công thức và lập luận toán cơ bản
- nhưng không được mặc định sinh viên đã quen với ngôn ngữ của textbook nghiên cứu
- mọi slide phải có đủ trực giác để theo được trên lớp

## Nguyên tắc không thương lượng

1. **Ít chữ**
- mỗi slide chỉ giữ lượng chữ cần thiết để giảng
- không biến slide thành ghi chú bài giảng

2. **Mỗi slide một ý chính**
- một slide chỉ nên trả lời một câu hỏi hoặc chốt một thông điệp
- nếu có hai ý ngang nhau, nên tách thành hai slide

3. **Tiếng Việt tự nhiên**
- ưu tiên diễn đạt như đang giảng cho sinh viên
- không dịch sát cấu trúc câu tiếng Anh
- chỉ giữ tiếng Anh khi đó là thuật ngữ thật sự cần thiết

4. **Phần phụ phải được đánh dấu**
- nội dung không cần giảng trên lớp nên gắn badge `📖 Tự học`

5. **Visual language thống nhất**
- màu sắc, spacing, caption, badge, hộp nhấn, tiêu đề phải cùng một hệ

## Những điều bị cấm hoặc nên tránh mạnh

1. **Bullet dài**
- một bullet dài quá hai dòng là tín hiệu xấu
- nếu ý dài, đổi sang câu ngắn hoặc tách slide

2. **Slide dày chữ**
- nếu người xem phải đọc quá 10-12 dòng liên tục, slide đang quá nặng

3. **Nhiều ý trong một slide**
- “định nghĩa + trực giác + ví dụ + cảnh báo” trong cùng một slide thường là sai

4. **Hình nhỏ**
- hình minh hoạ mà phải nheo mắt mới đọc được thì xem như chưa đạt

5. **Caption mơ hồ**
- caption không được chỉ mô tả “đây là hình gì”
- caption phải chốt được “hình này cho thấy điều gì”

## Cấu trúc chuẩn của một deck 120-130 phút

Một deck lý thuyết chuẩn nên có:

1. **Mở bài**
- tiêu đề
- nội dung / agenda
- 1-2 slide tạo động lực hoặc trực giác

2. **Các phần nội dung chính**
- mỗi phần có slide mở phần
- mỗi phần có một trục câu chuyện rõ

3. **Phần kết**
- tổng kết
- khi nào dùng gì / điểm chốt thực dụng
- tài liệu tham khảo nếu cần

### Số lượng slide gợi ý

Không có một con số cứng, nhưng với 120-130 phút:
- khoảng **35-45 slide thực dạy** là vùng an toàn
- nếu deck có trên 45 slide, phải có chiến lược `📖 Tự học` hoặc lướt nhanh

### Nhịp hợp lý

Một phần nên đi theo nhịp:
- **động lực**
- **ý tưởng**
- **cơ chế / công thức**
- **ví dụ**
- **cảnh báo / khi nào dùng**

Không nên đi theo nhịp:
- **định nghĩa**
- **định lý**
- **công thức**
- **thuật toán**
- **ví dụ**

vì như vậy sinh viên dễ mất trực giác từ sớm.

## Tiêu chuẩn ở mức section

Mỗi phần lớn phải trả lời được ba câu hỏi:

1. Phần này giải quyết vấn đề gì?
2. Nó nối với phần trước ra sao?
3. Sau phần này sinh viên phải nhớ điều gì?

### Slide mở phần phải làm gì

Slide mở phần không chỉ để đánh số.

Nó nên giúp sinh viên chuẩn bị tâm trí:
- đây là chủ đề gì
- tại sao phải học nó
- nó nằm ở đâu trong câu chuyện chung

Nếu phần mới mở ra một bước mới trong pipeline, nên có một slide cầu nối ngắn.

## Tiêu chuẩn ở mức slide

## 1. Mỗi slide phải có một câu chốt ẩn

Trước khi viết slide, phải trả lời:
- nếu sinh viên chỉ nhớ **một câu** sau slide này, câu đó là gì?

Nếu không trả lời được, slide chưa đủ rõ.

## 2. Mỗi slide chỉ nên có một loại tải chính

Một slide chỉ nên có **một thứ làm trung tâm**:
- hình
- công thức
- bảng so sánh
- quy trình
- ví dụ

Nếu slide có cả hình, cả công thức, cả 6 bullet, gần như chắc chắn cần tách.

## 3. Dấu hiệu slide đang quá tải

Slide nên bị xem là quá tải nếu có một trong các dấu hiệu:
- trên 3 bullet chính
- có bullet dài quá 2 dòng
- có nhiều hơn 1 công thức độc lập
- có 2 hình trở lên mà không có quan hệ so sánh rõ ràng
- có text nhỏ phải giảm font để “nhét vừa”
- có cả trực giác, chi tiết kỹ thuật, và ví dụ cùng lúc

Khi gặp các dấu hiệu này:
- tách slide
- hoặc xác định một ý là phụ và bỏ đi

## 4. Mật độ chữ

### Mức tốt
- 1 câu mở đầu ngắn
- 2-3 bullet ngắn
- hoặc 1 hình lớn + 1 caption

### Mức chấp nhận được
- 1 đoạn ngắn + 1 công thức + 2 bullet

### Mức xấu
- 1 đoạn dài
- 4-6 bullet
- chú thích nhỏ
- công thức dài
- hình nhỏ ở góc

## Quy tắc về wording

## 1. Viết như đang giảng, không như đang dịch

Ưu tiên:
- câu chủ động
- nhịp nói tự nhiên
- mệnh đề ngắn

Tránh:
- câu bị động nặng
- cấu trúc “theo textbook”
- mô phỏng cú pháp tiếng Anh

Ví dụ tốt:
- `Bagging giảm phương sai bằng cách trung bình hoá nhiều cây.`

Ví dụ xấu:
- `Sự giảm phương sai được đạt được thông qua quá trình lấy trung bình trên nhiều cây.`

## 2. Dùng thuật ngữ tiếng Anh có chọn lọc

Giữ tiếng Anh khi:
- đó là tên chuẩn mà sinh viên sẽ gặp lại
- dịch sang tiếng Việt làm tối nghĩa hơn

Ví dụ thường nên giữ:
- bagging
- boosting
- random forest
- impurity
- bias
- variance

Ví dụ nên Việt hoá:
- training error
- test error
- split
- leaf
- branch
- validation set

Nguyên tắc:
- hoặc Việt hoá rõ ràng
- hoặc giữ tiếng Anh có chủ đích
- không pha trộn lộn xộn trong cùng một cụm

## 3. Không dùng câu quá mạnh khi bản chất chỉ là “thường”

Ví dụ nên tránh:
- `Boosting chính xác nhất`
- `K-means cho kết quả tốt hơn`
- `BIC luôn chọn mô hình nhỏ hơn`

Nên sửa thành:
- `thường cho độ chính xác cao`
- `có thể phù hợp hơn`
- `thường phạt mạnh hơn nên hay chọn mô hình nhỏ hơn`

## 4. Mỗi bullet phải là một ý trọn vẹn

Bullet tốt:
- `Random Forests giảm tương quan giữa các cây bằng cách chỉ xét một tập đặc trưng ngẫu nhiên tại mỗi phép chia.`

Bullet xấu:
- `Giảm tương quan giữa các cây`

Bullet xấu vì:
- không tự đứng được
- phải đoán ý

## Quy tắc về hình ảnh

## 1. Hình phải làm việc thật sự

Mỗi hình phải có ít nhất một vai trò rõ:
- tạo trực giác
- minh hoạ một cơ chế
- cho ví dụ
- so sánh hai phương pháp
- làm nổi một cảnh báo

Nếu hình chỉ để “làm slide đỡ trống”, nên bỏ.

## 2. Hình phải đủ lớn

Hình tốt:
- là phần trung tâm của slide
- các chi tiết đọc được ở chế độ trình chiếu

Hình xấu:
- bị ép nhỏ để nhường chỗ cho quá nhiều chữ
- có text trong hình nhỏ hơn caption

Khi phải chọn:
- giảm chữ
- không giảm hình

## 3. Không dùng caption mơ hồ

Caption tốt:
- `Cắt cây ở các mức khác nhau sẽ cho số cụm khác nhau.`
- `Dữ liệu tuyến tính: mô hình tuyến tính khớp tốt hơn cây.`

Caption xấu:
- `Ví dụ minh hoạ`
- `Dendrogram ví dụ`
- `So sánh các phương pháp`

## 4. Hình phải khớp thông điệp của slide

Một slide có tiêu đề `Không cần chọn trước K` thì hình phải giúp người xem thấy ngay:
- cùng một cấu trúc
- nhưng có thể lấy ra nhiều số cụm khác nhau

Nếu hình không đỡ cho tiêu đề, thay hình hoặc đổi tiêu đề.

## 5. Nếu hình được sinh bằng script, ưu tiên sửa ở nguồn

Khi có lỗi:
- chồng lấn chữ
- mũi tên lệch
- title sai thứ tự
- màu sắc không nhất quán

thì ưu tiên sửa script sinh hình, không sửa crop hoặc vá tay nếu không cần thiết.

## Quy tắc về công thức

## 1. Công thức chỉ xuất hiện khi giúp hiểu

Chỉ giữ công thức nếu nó làm được ít nhất một trong ba việc:
- định nghĩa đúng bản chất
- giải thích cơ chế
- kết nối với một công thức sinh viên đã biết

Nếu công thức chỉ để “đúng sách”, nên lược bớt.

## 2. Một slide không nên có nhiều công thức ngang vai

Nếu có hai công thức mà cả hai đều quan trọng:
- tách slide
- hoặc một công thức chính, một công thức phụ trong lời giảng

## 3. Công thức phải có câu dẫn và câu chốt

Không được để công thức rơi từ trên trời xuống.

Cần đủ ba thành phần:
- câu dẫn: tại sao đang nhìn công thức này
- công thức
- câu chốt: công thức nói điều gì

Ví dụ:
- `Tại sao tương quan giữa các cây lại quan trọng? Hãy xem phương sai của trung bình nhiều cây:`
- công thức
- `Muốn giảm phương sai thật sự, phải giảm tương quan giữa các cây.`

## 4. Ký hiệu phải nhất quán

Không đổi ký hiệu giữa các slide nếu không cần.

Nếu đã dùng:
- \(K\) cho số cụm
- \(m\) cho số đặc trưng xét tại mỗi split
- \(B\) cho số cây

thì giữ nhất quán đến hết phần đó.

## Quy tắc về ví dụ

## 1. Ví dụ phải phục vụ ý chính, không được mở nhánh mới

Ví dụ tốt:
- minh hoạ đúng khái niệm vừa giới thiệu
- không cần giải thích thêm 3 tầng bối cảnh

Ví dụ xấu:
- vừa giới thiệu khái niệm mới
- vừa có dataset lạ
- vừa đòi giải thích domain

## 2. Mỗi ví dụ chỉ nên phục vụ một thông điệp

Ví dụ:
- `Hitters` để minh hoạ cây hồi quy
- `Heart` để minh hoạ cây phân lớp
- không nên bắt một ví dụ gánh quá nhiều vai

## 3. Ví dụ trong slide nên chốt điều rút ra

Không chỉ cho ảnh / plot.

Phải có một câu kiểu:
- `CV chọn cây khoảng 6 nút`
- `Single linkage tạo cụm dạng chuỗi`
- `Boosting cải thiện rõ hơn bagging trên dữ liệu này`

## Quy tắc về bảng

Bảng chỉ nên dùng khi thật sự cần so sánh theo nhiều tiêu chí.

### Bảng tốt khi:
- số cột ít
- mỗi ô ngắn
- dùng để ra quyết định

### Bảng xấu khi:
- mỗi ô là một câu dài
- người xem phải đọc như đọc văn bản

Nếu bảng được dùng để tổng kết:
- ưu tiên `khi nào dùng`
- `ưu điểm`
- `nhược điểm`
- `tuning`

Không nên biến bảng thành bản tóm tắt cả chương.

## Quy tắc về badge `📖 Tự học`

## Khi nào gắn

Gắn badge khi slide:
- là chi tiết kỹ thuật phụ
- là ví dụ mở rộng
- là benchmark / case phụ
- không cần để theo kịp mạch chính trên lớp

## Khi nào không gắn

Không gắn nếu slide:
- là bản lề logic
- chứa khái niệm lõi
- cần để hiểu slide sau

## Cách dùng

Dùng đúng pattern đã chuẩn hoá trong CSS:

```html
<div class="slide-badge-row"><span class="self-study-badge">📖 Tự học</span></div>
```

Đặt ngay sau `<h2>`.

Không dùng inline style riêng cho badge.

## Visual language

## 1. Màu sắc

Một lecture nên có một hệ màu nhất quán:
- màu chính
- màu nhấn
- màu cảnh báo
- màu trung tính

Ví dụ:
- xanh lam: cấu trúc / định nghĩa
- cam: cảnh báo / điểm chốt
- xanh lá: ví dụ tốt / lựa chọn phù hợp

Không đổi mapping màu tùy tiện giữa các slide cùng một phần.

## 2. Hộp nhấn

Hộp nhấn chỉ nên dùng cho:
- insight quan trọng
- cảnh báo
- nguyên tắc chốt

Không dùng hộp nhấn cho mọi thứ, nếu không sẽ mất tác dụng.

## 3. Font size

Không giảm font chỉ để nhét nhiều nội dung.

Nếu phải giảm font để vừa:
- gần như chắc chắn nên tách slide

## 4. Căn lề và spacing

Deck phải có nhịp đều:
- khoảng cách giữa title và body
- khoảng cách caption
- khoảng cách giữa hai cột
- khoảng cách trong lists

Spacing không đều làm deck nhìn kém chắc tay, dù nội dung đúng.

## Tiêu chuẩn kỹ thuật cho Reveal.js / HTML

## 1. Không lạm dụng inline style

Inline style chấp nhận được khi:
- chỉnh đặc thù cho một slide
- layout thật sự đặc biệt

Không nên:
- lặp cùng một block style ở nhiều slide
- tự phát minh badge / note / callout mới bằng inline style

Khi pattern lặp lại:
- đưa vào CSS chung

## 2. Asset phải có nguồn tái sinh

Nếu hình được sinh bằng code:
- giữ script trong `img/.../scripts`
- sửa bằng script, không vá ảnh bằng tay nếu tránh được

## 3. Cache busting

Khi asset SVG/PNG được render lại nhưng file name giữ nguyên:
- thêm hoặc tăng query string nếu cần để tránh cache khi preview

## 4. Tính nhất quán giữa slide và asset

Nếu slide nói:
- `Average / Single / Complete`

thì:
- caption
- title trong ảnh
- thứ tự panel
- màu của legend

phải cùng một mapping.

## Rubric rà soát một lecture

## A. Ở mức deck

1. Deck có một câu chuyện rõ từ đầu đến cuối không?
2. Có phần nào bị nặng hơn nhu cầu dạy thực tế không?
3. Có slide nào là “notes” trá hình không?
4. Phần nào nên gắn `📖 Tự học`?
5. Có slide tổng kết đủ thực dụng không?

## B. Ở mức section

1. Mỗi phần có mục tiêu rõ không?
2. Phần mới có được nối với phần trước không?
3. Có slide bản lề khi đổi chủ đề lớn không?

## C. Ở mức slide

1. Slide này có một ý chính rõ không?
2. Hình / công thức / bullet nào là trung tâm?
3. Nội dung có quá dày không?
4. Có thể bỏ bớt 30% chữ mà vẫn giữ ý không?
5. Caption có thật sự nói điều hình đang chứng minh không?

## D. Ở mức wording

1. Có câu nào dịch sát tiếng Anh không?
2. Có câu nào khẳng định quá mạnh không?
3. Thuật ngữ có nhất quán không?
4. Sinh viên năm 1-2 có theo được câu này khi nghe trên lớp không?

## E. Ở mức visual

1. Hình có đủ lớn không?
2. Có chỗ nào chồng lấn / quá sát / khó đọc không?
3. Màu có nhất quán không?
4. Hộp nhấn có dùng đúng chỗ không?

## Quy trình chuẩn khi tạo hoặc sửa slide

## Khi tạo slide mới

1. Viết câu chốt của slide
2. Chọn loại slide:
- hình
- công thức
- bảng
- ví dụ
- quy trình
3. Bỏ mọi ý không phục vụ câu chốt
4. Viết wording ngắn và tự nhiên
5. Kiểm tra xem có cần tách slide không

## Khi review slide cũ

1. Xác định slide đang cố làm mấy việc
2. Nếu hơn một việc, tách hoặc bỏ
3. Kiểm tra sự khớp giữa title, body và hình
4. Kiểm tra chỗ nào là textbook-speak
5. Đánh dấu `📖 Tự học` nếu không phải lõi

## Câu hỏi tự kiểm cuối cùng

Trước khi chốt một slide, tự hỏi:

1. Slide này có một ý chính rõ không?
2. Sinh viên có nhìn vào và biết mình đang học cái gì không?
3. Nếu bỏ bớt 20-30% chữ, slide có tốt hơn không?
4. Hình có đủ lớn để làm việc thật không?
5. Caption có chốt đúng thông điệp không?
6. Nếu giảng trên lớp, slide này giúp mình nói dễ hơn hay làm mình phải giải thích hộ slide?

Nếu câu 6 trả lời là:
- `phải giải thích hộ slide`

thì slide chưa đạt.

## Kết luận

Một deck tốt cho môn Học máy không phải là deck đầy đủ nhất.

Nó là deck:
- giúp giảng viên giữ được câu chuyện
- giúp sinh viên bám được logic
- và làm nổi bật đúng những ý đáng nhớ

Trong ngữ cảnh môn này, ưu tiên luôn là:
- **dễ dạy**
- **đúng bản chất**
- **ít chữ nhưng rõ ý**
