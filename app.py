# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
    Desc     : 语雀备份脚本-入口
-------------------------------------------------
"""
from yuque_doc_backups import init_token, fetch_user_id, fetch_repo_list, fetch_toc_list, doc_count
from yeque_md_to_local import new_md_to_local, search_all_file, md_to_local, pic_url_path_record_list, download_pic
import asyncio
import time

# 备份分为两个阶段
# 第一阶段下载的文档内图片是未修改的(远程url)----这个文档在第二阶段可以重复使用(只要下载后远程文档未修改)
# 第二阶段是根据下载的文档进行备份并下载图片到本地,两种方式
if __name__ == '__main__':
    yq_token = input("请输入你的语雀Token:")
    if len(yq_token) == 0:
        exit("请输入正确的Token!")
    init_token(yq_token)
    start_time = time.time()
    
    img_params = input("是否同步图片数据到本地(0:文件备份,1:文件备份+本地化):")
    if img_params == '0' or img_params == '1':
        
        # 第一阶段----下载文档(注意:如果有子文档,那么当前文档会是文件夹名(意味着丢失当前文档内容))
        # 如果远程已经下载并且未改变,那么可以注释以下

        yq_user_id = fetch_user_id()
        print("开始执行文档备份，请稍等...")
        yq_repo_list = fetch_repo_list(yq_user_id)

        for yq_repo in yq_repo_list:
           # 可以自定义处理的内容
            # if yq_repo.repo_name=='博客整理':
            #     continue
            print("开始拉取【{}】仓库下的文档".format(yq_repo.repo_name))
            fetch_toc_list(yq_repo.repo_id, yq_repo.repo_name)
        print("文档备份完毕，共记备份文档【{}】篇,共计耗时：{:.2f}ms,开始执行Markdown文件批量本地化...".format(doc_count,(time.time() - start_time) * 1000))

        if img_params == '1':
            # 第二阶段
            yq_doc_file_list = search_all_file()
            print("共扫描到Markdown文件【{}】篇，开始批量本地化...".format(len(yq_doc_file_list)))

            # 第二个参数:True表示所有文档放一个文件夹,所有图片放一个文件夹,False表示图片随文档放入文件夹
            # md_to_local(yq_doc_file_list)
            new_md_to_local(yq_doc_file_list,False)
            loop = asyncio.get_event_loop()
            for pic_url_path_record in pic_url_path_record_list:
                split_list = pic_url_path_record.split("\t")
                loop.run_until_complete(download_pic(split_list[1], split_list[0]))
            print("语雀文档备份及Markdown本地化已执行完毕,共计耗时：{:.2f}ms, 快去打开文件看看吧😄~".format(
                (time.time() - start_time) * 1000))
    else:
        exit("未输入正确参数,结束程序...")
    
