require 'digest'

module Jekyll::HashFilter
  def to_hash(input)
    if input != nil
      return Digest::MD5.hexdigest input
    end
    return ''
  end
end

Liquid::Template.register_filter(Jekyll::HashFilter)