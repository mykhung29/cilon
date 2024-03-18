# Xây dựng NFAε
trang_thai = {'q0', 'q1', 'q2'}
bang_chu_cai = {'0', '1'}
chuyen_trang_thai = {
    'q0': {'0': {'q0'}, None: {'q1'}},
    'q1': {'1': {'q1', 'q2'}},
    'q2': {'0': {'q2'}}
}
trang_thai_bat_dau = 'q0'
trang_thai_chap_nhan = {'q1'}

# Hàm tính đóng epsilon
def epsilon_closure(trang_thai_hien_tai):
    dong_epsilon = set()
    dong_epsilon.add(trang_thai_hien_tai)
    ngan_xep = [trang_thai_hien_tai]

    while ngan_xep:
        trang_thai_hien_tai = ngan_xep.pop()
        if trang_thai_hien_tai in chuyen_trang_thai and None in chuyen_trang_thai[trang_thai_hien_tai]:
            chuyen_epsilon = chuyen_trang_thai[trang_thai_hien_tai][None]
            for trang_thai_epsilon in chuyen_epsilon:
                if trang_thai_epsilon not in dong_epsilon:
                    dong_epsilon.add(trang_thai_epsilon)
                    ngan_xep.append(trang_thai_epsilon)

    return dong_epsilon

# Hàm tính trạng thái tiếp theo
def trang_thai_tiep_theo(trang_thai_hien_tai, ki_tu):
    trang_thai_tiep_theo = set()

    for trang_thai in trang_thai_hien_tai:
        if trang_thai in chuyen_trang_thai and ki_tu in chuyen_trang_thai[trang_thai]:
            trang_thai_tiep_theo |= chuyen_trang_thai[trang_thai][ki_tu]

    dong_epsilon = set()
    for trang_thai in trang_thai_tiep_theo:
        dong_epsilon |= epsilon_closure(trang_thai)

    return dong_epsilon

# Hàm kiểm tra chuỗi
def chap_nhan(chuoi_nhap):
    trang_thai_hien_tai = epsilon_closure(trang_thai_bat_dau)

    for ki_tu in chuoi_nhap:
        trang_thai_hien_tai = trang_thai_tiep_theo(trang_thai_hien_tai, ki_tu)

    return any(trang_thai in trang_thai_chap_nhan for trang_thai in trang_thai_hien_tai)

# Kiểm tra chuỗi "001" có được chấp nhận bởi NFAε hay không
chuoi_nhap = "001"
if chap_nhan(chuoi_nhap):
    print(f'Chuỗi "{chuoi_nhap}" được chấp nhận bởi NFAε.')
else:
    print(f'Chuỗi "{chuoi_nhap}" không được chấp nhận bởi NFAε.')