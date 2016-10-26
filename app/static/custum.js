/**
 * Created by tienvu on 25/10/2016.
 */
$(function () {
    $(".delete").click(function () {
        var ids = $(this).attr('id');
        var url=$(this).attr('url');
        if (!confirm("Are you sure you want to delete this record")){
            return false
        }
            $.ajax({
                type:"POST",
                url:url,
                data:{ids:ids},
                success:function (resp) {
                    console.log(resp);
                },
                error:function (error) {
                    console.log(error);
                }
            });
            $(this).parents(".rowlist").animate({ backgroundColor: "#fbc7c7" }, "fast")
            .animate({ opacity: "hide" }, "slow");
        return false;
    })

})
$(function () {
    $(".edit").click(function () {
        var ids = $(this).attr('row_id');
        var url=$(this).attr('url');
            $.ajax({
                type:"POST",
                url:url,
                data:{ids:ids},
                success:function (resp) {
                    console.log(resp);
                },
                error:function (error) {
                    console.log(error);
                }
            });
        return false;
    })

})



