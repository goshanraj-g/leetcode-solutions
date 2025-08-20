# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    h1 = {}
    h2 = {}
    s.each_char do |x|
        if h1.key?(x)
            h1[x] += 1
        else
            h1[x] = 1
        end
    end

    t.each_char do |x|
        if h2.key?(x)
            h2[x] += 1
        else
            h2[x] = 1
        end
    end

    return h1 == h2
end
