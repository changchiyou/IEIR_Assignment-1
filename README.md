# How to run
step 0. (�p�w��*novel_data.csv*�i���L)��*spyder* Editer�B��άO�����N*solr_import.py*��*solr_retrieve.py*��i�P*python.exe*�P��m��Ƨ���A�H����Ƨ������|�}��cmd�������J�H�U���O�A�H���*novel_data.csv*��ơG
<pre><code>python solr_scraping.py
</code></pre>
step 1. ����*solr-7.7.0/bin*��Ƨ�����*start.bat*�A�T�굥��"Happy search!"�r�˶]�X��

step 2. ���s�����i�J *http://127.0.0.1:8983/solr/#/* �A�bCore Admin�s�W�@��Core�W��*Assignment1*�A�æbSchema���O�s�W*question*�M*answer* Field�Afield type�Ҭ�text_general�C

step 3. ��0.�B�J�}�Ҫ�cmd������J�H�U���O(���B�J��i��ݭn�����Ҧ������᭫�s����1.�B�J)�G
<pre><code>python solr_import.py
</code></pre>

step 4. ���s���s�����i�J *http://127.0.0.1:8983/solr/#/* ��A�T�{Query����I��Execute Query���s�ᦳ�S����ܽT��ɤJ�F*solr_import.py*����*QA_Pair_list*�A�é�3.�B�J�}�Ҫ�cmd������J�H�U���O�G
<pre><code>python solr_retrieve.py
</code></pre>
step 5. ��Jpaper���ĥ|�IExperiment�U���Ѫ��Q�I����input�C

