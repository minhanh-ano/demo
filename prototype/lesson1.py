
from ortools.sat.python import cp_model

# Tao mo hinh bai toan
model = cp_model.CpModel()

# Khai bao thoi diem bat dau va ket thuc
start_A = model.new_int_var(0, 10, "start_A")
end_A = model.new_int_var(0, 10, "end_A")

start_B = model.new_int_var(0, 10, "start_B")
end_B = model.new_int_var(0, 10, "end_B")

# Quy dinh thoi luong
model.add(end_A == start_A + 3)
model.add(end_B == start_B + 2)

# B chi duoc bat dau khi A ket thuc
model.add(start_B >= end_A)

# Muc tieu: hoan thanh som nhat
model.minimize(end_B)

# Chay bo giai
solver = cp_model.CpSolver()
status = solver.solve(model)

# In ket qua
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print("Cong viec A:")
    print("  Bat dau:", solver.value(start_A))
    print("  Ket thuc:", solver.value(end_A))

    print("Cong viec B:")
    print("  Bat dau:", solver.value(start_B))
    print("  Ket thuc:", solver.value(end_B))

    print("Trang thai:", solver.status_name(status))
else:
    print("Khong tim duoc lich kha thi.")

