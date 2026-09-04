# Gói Canvas (Common Cartridge) — template lịch trình chung

Sinh file `.imscc` từ bảng lịch trong `<kỳ>/index.html` để import vào **mọi lớp** Canvas của môn.
Gói **không gắn ngày giờ** (thời khoá biểu từng lớp tự đặt), chỉ gồm:

- **Modules** — 1 module/tuần theo cột Tuần ↔ Bài của `index.html`: link slide, notebook bài giảng (Colab),
  notebook lab (Colab); cộng module "Bắt đầu" (trang môn học, chính sách AI, đề BTL, trang Lịch giảng dạy)
  và module "Bài tập lớn" (đề + 4 mốc, chưa có ngày).
- **Trang wiki "Lịch giảng dạy"** — bảng Tuần | Bài giảng | Notebook, link tuyệt đối về `courses.iaidev.com`.
- **Syllabus** — giới thiệu, cơ cấu điểm 10/10/20/60, bảng lịch.

Mọi link trỏ ra site public, nên gói không chứa học liệu và không cần cập nhật khi sửa slide;
chỉ chạy lại khi **đổi bảng lịch** trong `index.html`.

## Chạy

```bash
.venv/bin/python tools/canvas/make_canvas_package.py              # → tools/canvas/dist/ltxldl-2627-1-canvas-template.imscc
.venv/bin/python tools/canvas/make_canvas_package.py --term 2627-1 --out /tmp/canvas
```

Chỉ dùng thư viện chuẩn Python. `tools/canvas/dist/` là sản phẩm sinh ra — không commit.

## Import lên Canvas

1. Vào course → **Settings → Import Course Content**.
2. Content Type: **Common Cartridge 1.x Package** → chọn file `.imscc`.
3. Content: **Select specific content** rồi tick *Modules*, *Pages*, *Syllabus Body*; bỏ *Course Settings*
   nếu không muốn gói đổi trang chủ course sang Modules / múi giờ Asia/Ho_Chi_Minh.
4. Import lại gói mới (sau khi đổi lịch) sẽ **cập nhật** module/trang cũ chứ không nhân đôi,
   vì ID được băm từ nội dung (ổn định giữa các lần chạy).

Sau khi import, mỗi lớp tự thêm ngày cho các mốc BTL/kiểm tra (Calendar hoặc Assignments) — gói cố tình
không tạo Assignment để không sinh cột điểm thừa trong Gradebook.

## Không đưa vào gói (chủ đích)

- Tuần kiểm tra giấy (3, 9) — quy ước công khai chỉ ghi "2 bài", mốc tuần thông báo riêng trên Canvas.
- Đáp án lab, giáo án TA (`2627-1/private/`) — gửi TA qua Canvas, không nằm trong template.
