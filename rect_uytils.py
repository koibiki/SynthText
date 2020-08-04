def is_ray_intersects_segment(poi, s_poi, e_poi):  # [x,y] [lng,lat]
    # 输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    if s_poi[1] == e_poi[1]:  # 排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if s_poi[1] > poi[1] and e_poi[1] > poi[1]:  # 线段在射线上边
        return False
    if s_poi[1] < poi[1] and e_poi[1] < poi[1]:  # 线段在射线下边
        return False
    if s_poi[1] == poi[1] and e_poi[1] > poi[1]:  # 交点为下端点，对应spoint
        return False
    if e_poi[1] == poi[1] and s_poi[1] > poi[1]:  # 交点为下端点，对应epoint
        return False
    if s_poi[0] < poi[0] and e_poi[1] < poi[1]:  # 线段在射线左边
        return False

    xseg = e_poi[0] - (e_poi[0] - s_poi[0]) * (e_poi[1] - poi[1]) / (e_poi[1] - s_poi[1])  # 求交
    if xseg < poi[0]:  # 交点在射线起点的左侧
        return False
    return True  # 排除上述情况之后


def is_in_rect_inter(point, rect):
    intersect = is_ray_intersects_segment(point, rect[0], rect[1])
    intersect += is_ray_intersects_segment(point, rect[1], rect[2])
    intersect += is_ray_intersects_segment(point, rect[2], rect[3])
    intersect += is_ray_intersects_segment(point, rect[3], rect[0])
    return intersect % 2


def has_interact(rect1, rect2):
    for point in rect1:
        if is_in_rect_inter(point, rect2):
            return True
    return False
