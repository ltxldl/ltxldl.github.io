# Nguyên tắc sửa văn phong slide — rút từ lượt duyệt buổi 1 của giảng viên

> **Mục đích:** chuẩn cho pass sửa văn phong **14 deck còn lại (buổi 2–15)**. Nguồn: diff giữa bản Claude dựng (commit `e0a577f`) và bản giảng viên duyệt buổi 1 (06–07/07/2026). Nhận xét chung của GV: *nội dung ổn, văn phong kém*.
>
> **Phạm vi pass:** chỉ sửa văn phong + các quy ước liệt kê dưới đây. **Không** đổi cấu trúc slide, thứ tự nội dung, nội dung kỹ thuật, code/output — trừ comment tiếng Việt trong code khi dính quy tắc văn phong. Buổi 1 đã được GV sửa tay — không đụng nữa, chỉ dùng làm mẫu đối chiếu.

## 1. Quy ước toàn cục (áp máy móc cho mọi deck)

| Quy ước | Trước | Sau |
|---|---|---|
| Bỏ số tiểu mục ở mọi `<h2>` (giữ số to ở slide mở phần trong `<h1>`) | `2.3. Notebook: …` | `Notebook: …` |
| Slide agenda | `Hôm nay` | `Tổng quan` |
| Tiêu đề hộp `key-box` | `Điểm chốt` | `Quan trọng` |
| Mục AI cuối deck (heading + text trong `.ai-badge`) | `Làm với AI` / `Làm với AI thì sao?` | `Làm việc với AI` / `Làm việc với AI thì sao?` |
| Mốc thời gian tương đối | `notebook hôm nay` | `notebook buổi này` |
| Kênh lớp | `Canvas` | `Canvas Portal` |
| Tên file viết đầy đủ | `AI_USAGE` | `AI_USAGE.md` |

Ngoài ra: component `.pipeline` đang quá khổ — GV phải chèn inline `style="font-size: 0.7em;"` hai lần ở buổi 1. Trong pass: **giảm cỡ mặc định của `.pipeline` trong `lecture-style.css` một lần**, rồi bỏ các inline style đó (kể cả 2 chỗ ở buổi 1).

## 2. Giọng văn: trung tính, chính xác, bớt "diễn"

- **Bỏ ẩn dụ lạ**, gọi thẳng tên khái niệm: "con đường từ thô đến giá trị" → "quá trình từ dữ liệu thô đến quyết định"; "'tiếng mẹ đẻ' của cả AI" → "ngôn ngữ chính của cả ngành AI"; venv là "'hộp' thư viện" → "môi trường / bộ thư viện tách biệt" (sửa cả trong comment code: "tạo hộp" → "tạo môi trường tại thư mục .venv").
- **Bỏ từ đệm giật tít** ở đầu tiêu đề/subtitle: "Sự thật: AI viết code rất khá" → "AI viết code dữ liệu rất tốt"; subtitle "Chuyện phải nói thẳng ngay buổi đầu." → câu nêu đúng nội dung ("Minh bạch với AI: khai báo, hiểu, kiểm chứng.").
- **Bỏ emoji đùa** trong câu (😉); emoji chức năng (🔒 🔓 🤖 ⚠️ 📖) giữ nguyên.
- **Bớt khẩu ngữ ăn thua/suồng sã**: "thắng thua ở sản phẩm" → "được quyết định bởi sản phẩm"; "làm tử tế" → "làm tốt"; "cứ bấm đã" → "cũng có thể chạy để xem kết quả"; "AI được chào đón" → "AI được phép sử dụng"; "giấu mới là vấn đề" → "giấu diếm là vấn đề".
- **Không triệt tiêu hết cá tính**: ví dụ sinh động được giữ ("dữ liệu bẩn → kết luận… cũng bẩn"); thành ngữ dễ hiểu giữ kèm chú giải trong ngoặc ("giẫm chân nhau (xung đột thư viện)").

## 3. Câu đầy đủ, đủ chủ–vị

- Câu tỉnh lược → câu có chủ ngữ + động từ: "Tài liệu sống, chạy từng ô" → "Notebook là một tài liệu sống, có thể chạy từng ô"; "Lịch sử mọi thay đổi của code" → "Git ghi lại lịch sử mọi thay đổi của code".
- Thêm "có thể / sẽ / được / này" cho câu tròn: "Muốn làm cả hai" → "Muốn làm được cả hai điều này"; "máy khác dựng lại y hệt" → "máy khác có thể dựng lại y hệt".
- Dùng "→" cho quan hệ nhân quả/chuỗi thay cho "—": "Dữ liệu thô → dữ liệu sạch → thông tin → quyết định."

## 4. Thuật ngữ & ngôi xưng

- Ngôi nhất quán **"bạn"**: "máy mình" → "máy bạn".
- Term Anh thông dụng giữ nguyên, không dịch gượng: "trên mây" → "trên cloud".
- Từ chuẩn mực hơn: "Trước nó / Sau nó" → "Tiên quyết / Sau môn này"; "3 nghĩa vụ" → "3 trách nhiệm".
- Tiêu đề dạng câu hỏi viết tự nhiên: "Dữ liệu thật trông như thế này" → "Dữ liệu thật nhìn thế nào?".

## 5. Trình bày

- `<h1>` dài: chèn `<br />` tại điểm ngắt ngữ nghĩa (GV làm ở cả title slide và tiêu đề bài).
- Title slide: thông tin kỳ học viết trơn, bỏ label đậm ("**Học kì:** 1, …" → "Học kì 1, …").
- Chi tiết chưa chốt thì không hứa cụ thể: "quiz 3 câu về nó" → "quiz kiểm tra".

## 6. Việc kèm theo pass (bắt buộc)

1. Sau khi sửa chữ, **chạy lại kiểm tra tràn khung 960×700** (Playwright, như đợt dựng) trên toàn bộ deck đã sửa — câu dài ra dễ gây tràn.
2. Slide "Kế hoạch mỗi tuần" (mọi deck nào nhắc nhịp tuần): cập nhật theo cấu trúc **2 tiết lý thuyết + 2 tiết thực hành** — nội dung cụ thể theo kế hoạch giờ thực hành (xem CLAUDE.md khi đã chốt).
3. Deck nào có mục tự đánh giá cấu trúc ("Hôm nay", badge…) thì cập nhật đồng bộ với quy ước mục 1.
