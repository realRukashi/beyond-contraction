# Câu chuyện nghiên cứu — bản giải thích tiếng Việt

## Từ trực giác ban đầu đến kết luận cuối

Điểm xuất phát là một trực giác đơn giản: một từ đa nghĩa như **bank** không thật sự có một nghĩa cố định. Nếu chưa có ngữ cảnh, `bank` có thể là ngân hàng hoặc bờ sông. Vì vậy ta có thể hình dung nghĩa của từ như một **vùng khả năng** thay vì một điểm duy nhất. Khi ngữ cảnh được thêm vào, ví dụ `mortgage`, số cách hiểu hợp lý giảm xuống. Trực giác ban đầu vì thế là:

\[
R_0 \supset R_1 \supset R_2,
\]

hay nói nôm na: **ngữ cảnh càng rõ, vùng nghĩa càng co lại**.

Nhưng contextual encoder như BERT không biểu diễn “phân phối xác suất trên các nghĩa” trực tiếp. Với mỗi lần xuất hiện của từ trong một câu, mô hình tạo ra một vector riêng. “Đám mây” chỉ xuất hiện khi gom nhiều câu lại. Vì thế hai câu đều chắc chắn dùng `bank` theo nghĩa tài chính vẫn có thể có vector khá khác nhau, vì một câu nói về mortgage còn câu kia nói về recession, collapse, employees, location, v.v.

Điểm phân biệt quan trọng là:

\[
\boxed{\text{chắc chắn về sense} \neq \text{representation phải đồng nhất}}
\]

Ngữ cảnh vừa giúp **chọn đúng nghĩa**, vừa thêm **chi tiết về sự kiện và hoàn cảnh**.

## V2–V3: không phải co lại đơn giản

Các thí nghiệm có kiểm soát cho thấy khi thêm bằng chứng hữu ích để phân biệt nghĩa, phần ổn định nhất là **các sense trở nên tách biệt hơn**. Trong V3, between-sense differentiation tăng ở toàn bộ 45 tổ hợp model × layer × lượng context được tổng hợp. Tuy nhiên độ phân tán bên trong cùng một sense không có một quy luật chung: BERT, RoBERTa và DeBERTa-v3 cho các quỹ đạo khác nhau.

Điều này bác bỏ một kết luận quá đơn giản kiểu “disambiguation = contraction”.

## V4: cùng một context cũ, thêm đúng một cue mới

V4 sửa thiết kế để có thể hỏi một câu mạnh hơn: **khi sense trở nên rõ hơn thì thông tin context đã có trước đó đi đâu?**

Với cùng một occurrence, ta tạo một trạng thái nền `h0`, rồi thêm một cue chẩn đoán hoặc một cue control đã được match về vị trí/khoảng cách. Kết quả cho thấy cue chẩn đoán:

- tăng thông tin sense có thể đọc ra bằng probe;
- làm vector update hướng nhiều hơn vào subspace phân biệt sense;
- nhưng cũng làm cấu trúc representation thay đổi rộng hơn, chứ không chỉ di chuyển trên một “trục sense” duy nhất;
- thông tin context cũ vẫn gần như recover được bằng decoder mới, dù decoder cũ suy giảm và CKA với trạng thái trước cue giảm.

Vì vậy từ phù hợp hơn là **tái tổ chức representation**.

## V5: thử phá conclusion đó

V5 dùng ba kiểm tra cuối.

### 1. Natural, non-oracle context

Context được mở rộng tự nhiên theo khoảng cách tới từ mục tiêu (2 → 4 → 8 → 16 token), không dùng gold sense để chọn cue. Sense usable information vẫn tăng ở phần lớn các word-level transitions. Quan trọng hơn, những update làm sense information tăng nhiều hơn cũng thường có thành phần hướng vào sense subspace lớn hơn, đặc biệt rõ ở BERT và RoBERTa.

### 2. LEACE

LEACE được dùng để xóa phần **linearly accessible sense information** khỏi representation. Sense information giảm đáng kể, nhưng khả năng reconstruct context cũ chỉ giảm khoảng 1–1.5% tương đối. Điều này gợi ý sense information và context information **có liên hệ nhưng không trùng hoàn toàn**: chúng có thể tách được một phần trong không gian tuyến tính.

### 3. RAW-C

Trên 672 cặp ngữ cảnh tự nhiên của RAW-C, độ giống nhau giữa contextual embeddings có tương quan dương đáng kể với đánh giá relatedness của con người, và cosine similarity phân biệt same-sense/different-sense tốt hơn chance. Điều này cung cấp external semantic validity, nhưng không có nghĩa mô hình và con người dùng cùng một cơ chế.

## Kết luận dễ nhớ

Khi mô hình xác định được một từ đang mang nghĩa nào, nó **không đơn giản ép tất cả các trường hợp của nghĩa đó vào một cụm nhỏ**. Thay vào đó, representation được tổ chức lại sao cho sense phù hợp dễ đọc và dễ phân biệt hơn, trong khi phần lớn thông tin về context vẫn được giữ lại.

\[
\boxed{\text{lexical disambiguation} \approx \text{sense-directed representational reorganization}}
\]

chứ không phải:

\[
\boxed{\text{lexical disambiguation} = \text{simple contraction}}
\]

## Một câu để kể với người khác

> Tôi nghiên cứu điều gì xảy ra trong không gian embedding khi ngữ cảnh làm rõ nghĩa của một từ đa nghĩa. Trực giác ban đầu là representation sẽ co về một sense, nhưng các thí nghiệm cho thấy cơ chế giống một quá trình tái tổ chức hơn: sense trở nên dễ phân biệt hơn, vector update có hướng liên quan tới sense rõ hơn, nhưng phần lớn thông tin context khác vẫn còn được giữ lại.
