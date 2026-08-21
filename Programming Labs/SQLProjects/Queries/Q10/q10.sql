select u.usr, 'top in followers' as category
from users u
join follows f on u.usr = f.flwee
group by u.usr
having count(f.flwer) = (
    select max(follower_count)
    from (
        select flwee, count(flwer) as follower_count
        from follows
        group by flwee
    )
)
union
select t.writer, 'top in retweets' as category
from tstat t
group by t.writer
having avg(t.ret_cnt) = (
    select max(avg_retweets)
    from (
        select writer, avg(ret_cnt) as avg_retweets
        from tstat
        group by writer
    )
);
