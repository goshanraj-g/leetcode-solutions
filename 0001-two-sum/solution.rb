# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    hash = {}
    nums.each_with_index do |num, index|
        complement = target - num
        if hash.has_key?(complement)
            return [hash[complement], index]
        else
            hash[num] = index
        end
    end
    []
end
