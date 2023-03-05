nums1, nums2 = set(map(int, input().split())), set(map(int, input().split()))
nums = []
for num in nums1:
    if num in nums2:
        nums.append(num)
print(*sorted(nums))
# Сортировка пузырьком работает слишком медленно
