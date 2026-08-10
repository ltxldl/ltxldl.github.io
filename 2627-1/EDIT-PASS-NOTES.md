# Nguyên tắc sửa văn phong slide — rút từ lượt duyệt buổi 1 của giảng viên

> **Mục đích:** chuẩn cho pass sửa văn phong **14 deck còn lại (buổi 2–15)**. Nguồn: diff giữa bản agent dựng (commit `e0a577f`) và bản giảng viên duyệt buổi 1 (06–07/07/2026). Nhận xét chung của GV: *nội dung ổn, văn phong kém*.
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
- **Bỏ emoji đùa** trong câu (😉); emoji chức năng (🚫 ✅ 🤖 ⚠️ 📖) giữ nguyên; cặp chế độ đánh giá là 🚫 đóng / ✅ mở — QĐ GV 22/07/2026 thay cặp khoá 🔒/🔓 cũ vì hai khoá quá giống nhau, in đen trắng không phân biệt được; emoji chế độ luôn đi kèm chữ "đóng"/"mở".
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

1. Sau khi sửa chữ, **chạy lại kiểm tra tràn khung 960×700** trên toàn bộ deck đã sửa — câu dài ra dễ gây tràn. Serve repo (xem CLAUDE.md mục "Chạy preview"), mở deck ở viewport 960×700, rồi chạy đoạn dưới trong console trình duyệt (hoặc qua công cụ điều khiển trình duyệt). Nó đo **slide lá** — `section` không chứa `section` con; đếm cả `section` bọc vertical stack là sai — và bỏ qua `display:none` bằng cách hiện tạm từng slide:

   ```js
   (() => {
     const leaves = [...document.querySelectorAll('.reveal .slides section')].filter(s => !s.querySelector('section'));
     const bad = [];
     leaves.forEach((el, i) => {
       const chain = []; let n = el;
       while (n && n.tagName === 'SECTION') { chain.push(n); n = n.parentElement.closest('section'); }
       const saved = chain.map(c => c.style.cssText);
       chain.forEach(c => { c.style.display = 'block'; c.style.visibility = 'hidden'; });
       if (el.scrollHeight > 700 || el.scrollWidth > 960)
         bad.push({ slide: i + 1, h: el.scrollHeight, t: (el.querySelector('h1,h2') || {}).textContent });
       chain.forEach((c, k) => { c.style.cssText = saved[k]; });
     });
     return JSON.stringify({ total: leaves.length, overflow: bad });
   })()
   ```

   Kết quả phải là `overflow: []`; báo cáo dạng `0/N slide tràn`. Kiểm luôn hình đã load: `[...document.querySelectorAll('.reveal img')].map(i => [i.getAttribute('src'), i.complete && i.naturalWidth > 0])`.
2. Slide "Kế hoạch mỗi tuần" (mọi deck nào nhắc nhịp tuần): cập nhật theo cấu trúc **2 tiết lý thuyết + 2 tiết thực hành** — nội dung cụ thể theo kế hoạch giờ thực hành (xem CLAUDE.md khi đã chốt).
3. Deck nào có mục tự đánh giá cấu trúc ("Hôm nay", badge…) thì cập nhật đồng bộ với quy ước mục 1.

---

# Bổ sung v2 — rút từ lượt duyệt buổi 1–2 + ai-policy của giảng viên (22/07/2026)

> Nguồn: 7 commit `tune/update` của GV (`c9b841d`…`bb3cf31`). Áp cho pass duyệt-từng-buổi trước khi publish (buổi 3 trở đi). Các quy tắc v1 ở trên vẫn nguyên hiệu lực.

## 7. Chi tiết dễ thay đổi → nói mềm, chỉ giữ ở một nơi chính tắc

- Lịch kiểm tra cụ thể "tuần 3, 5, 7, 11, 13" → "**~5 tuần**" / "~5 bài kiểm tra giấy 15 phút" trong mọi học liệu hướng SV (con số tuần cụ thể chỉ nằm trong tài liệu nội bộ + công bố Canvas Portal khi có thời khoá biểu). Tương tự: bỏ "(buổi 9)", "(giám sát)"/"có giám sát".
- Trọng số % chỉ xuất hiện trong **bảng Cơ cấu điểm** (deck 1); mọi chỗ khác nhắc đầu điểm thì không kèm %.
- Nhãn đầu điểm theo tên đề cương: "Quiz trên lớp — ~5 bài kiểm tra giấy 15 phút".

## 8. Chế độ đóng/mở gắn với *hoạt động*, không gắn với đầu điểm

- "Bài tập lớn" trong danh sách chế độ mở → "**Làm bài tập lớn tại nhà**" (BTL tổng thể gồm cả vấn đáp đóng).
- Nhãn mục tự làm trong lab: "(làm sớm tại lớp hoặc làm tại nhà)" — không dùng "(làm xong sớm / về nhà)".

## 9. Giọng trung tính (nối dài mục 2) — danh sách thay cụ thể

- "cho tử tế" → "một cách có trách nhiệm" · "đàng hoàng" → "đầy đủ" · "gây lú" → "gây nhầm lẫn" · "như bạn tưởng" → "như bạn nghĩ" · "Ngoài đời" → "Thực tế hiện nay" · "hai thứ" → "hai quy tắc".
- "Quy tắc vàng" → "Quy tắc" · "Câu hỏi đáng ngẫm" → "Câu hỏi" hoặc "Câu hỏi tự học" · "Thử thách về nhà 🏆" → "Bài tập về nhà" (bỏ 🏆).
- **Cắt lời rao lặp**: "— thành phố sẽ đi cùng lớp đến hết môn", "— đúng nguồn dữ liệu của bài tập lớn", "đúng các lỗi bạn sẽ gặp trong bài tập lớn", "Hàm này sẽ theo bạn tới tận bài tập lớn", "loại câu hỏi bạn sẽ gặp trong vấn đáp", "— thuộc từ bây giờ, dùng đến hết môn", "(là) đủ cho môn này" → mỗi kết nối BTL/xuyên-môn chỉ nói **một lần** trong cả bộ học liệu, các chỗ lặp cắt thẳng.
- Xưng hô TA trong học liệu SV: "trợ giảng" → "**giảng viên thực hành**" (khi chỉ người dạy giờ thực hành; tên giờ học vẫn là "giờ thực hành").
- Bài debug không mách trước chỗ lỗi (bỏ comment kiểu `# <-- có gì đó sai sai`).
- Tên hình/caption ngắn gọn, không văn vẻ ("Chim to thì cánh dài — và mỗi loài một vùng riêng" → "Loài chim lớn thì cánh dài").
- Menu path rút gọn còn tên lệnh ("Runtime → Restart session and run all" → "Restart session and run all").
- "sau notebook này, bạn:" → "…, bạn sẽ:" (đủ trợ động từ trước danh sách mục tiêu).

## 9b. Thuật ngữ Việt hoá thêm (QĐ GV khi duyệt buổi 3, 22/07/2026)

- **percentile → phân vị**, **outlier → ngoại lai** trong văn xuôi/tiêu đề; lần đầu xuất hiện trong mỗi tài liệu chú thích ngoặc "(percentile)"/"(outlier)". Tên API (`np.percentile`), tên biến, chuỗi trong output giữ nguyên. Lưu ý buổi 10 (làm sạch dữ liệu) dùng dày đặc hai từ này — khi duyệt đến buổi 10 phải áp đồng bộ.

## 10. Slide code & tiêu đề (nối dài mục 5)

- Tiêu đề `<h2>` cắt từ đệm: "chuyện định dạng" → "định dạng"; "CSV 'bằng tay' — một lần để hiểu" → "CSV thủ công"; "Cạm bẫy số 1" → "Cạm bẫy 1"; "máy lọc dữ liệu thủ công" → "lọc dữ liệu thủ công".
- **Mỗi lệnh một cặp `jp-input`/`jp-output` riêng** — không gộp nhiều lệnh có output vào một cell; sau khi tách, đánh lại `data-jp-n` liên tục.
- Thuật ngữ viết tắt lần đầu xuất hiện: chú thích trong ngoặc ("QA (quality assurance)").

## 11. Hình minh hoạ: SVG, không PNG (QĐ GV 22/07/2026)

Mọi hình sinh bằng matplotlib phải xuất **SVG** (không PNG) với cấu hình chuẩn trong `img/lecture-XX/scripts/gen_figures.py`:

```python
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for f in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(f))
INK, MUTED = "#333333", "#666666"
plt.rcParams.update({"font.family": "Source Sans Pro", "svg.fonttype": "path",
                     "figure.facecolor": "none", "savefig.facecolor": "none", "text.color": INK})
```

- `svg.fonttype="path"` (chữ → outline) là **bắt buộc**: SVG nhúng qua `<img>` là tài liệu cô lập, không thấy font của trang → để `none` thì chữ rơi về serif.
- Nền trong suốt (`facecolor="none"`); viền/nhãn dùng `#333` (mực) và `#666`/`#777` (phụ) thay vì đen tuyền; màu nhấn lấy từ `lecture-style.css` (`#1E93AB`, `#E8890C`, `#2E8B57`).
- Sau khi sinh: đổi `src` trong deck sang `.svg`, `git rm` file PNG cũ, mở deck kiểm hình load được (`img.complete && naturalWidth > 0`) rồi đo tràn.
- **Đã áp**: buổi 3, 5. **Còn PNG, phải chuyển khi duyệt tới**: buổi 8 (2 hình), 10 (1), 12 (7), 13 (7).
