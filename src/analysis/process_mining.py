import os
import glob
import pm4py

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.statistics.start_activities.log import get as start_activities
from pm4py.statistics.end_activities.log import get as end_activities

def create_result_directory(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"'{directory}' klasörü oluşturuldu.")
    else:
        print(f"'{directory}' klasörü zaten mevcut.")


def analyze_event_logs(log_directory: str, result_directory: str):
    create_result_directory(result_directory)
    xes_files = glob.glob(os.path.join(log_directory, "*.xes"))

    if not xes_files:
        print(f"'{log_directory}' klasöründe .xes uzantılı dosya bulunamadı.")
        return

    for xes_file in xes_files:
        print(f"\nAnalyzing file: {xes_file}")

        file_name = os.path.splitext(os.path.basename(xes_file))[0]
        result_file = os.path.join(result_directory, f"{file_name}_analysis.md")

        with open(result_file, "w", encoding="utf-8") as md_file:
            md_file.write(f"# {file_name} Analiz Sonuçları\n\n")

            try:
                log = xes_importer.apply(xes_file)
                md_file.write("## Log Yükleme\n")
                md_file.write(f"{xes_file} dosyası başarıyla yüklendi.\n\n")
            except Exception as e:
                error_msg = f"Dosya yüklenirken hata oluştu: {e}"
                print(error_msg)
                md_file.write("## Log Yükleme\n")
                md_file.write(f"**Hata:** {error_msg}\n\n")
                continue

            # 3) Alpha Miner ile Process Model oluşturma
            try:
                net, im, fm = alpha_miner.apply(log)
                md_file.write("## Alpha Miner Sonuçları\n")
                md_file.write("Alpha Miner ile süreç modeli oluşturuldu.\n\n")
                md_file.write(f"{net, im, fm}\n\n")
            except Exception as e:
                error_msg = f"Alpha Miner çalışırken hata oluştu: {e}"
                print(error_msg)
                md_file.write("## Alpha Miner Sonuçları\n")
                md_file.write(f"**Hata:** {error_msg}\n\n")

            # 4) Heuristic Miner ile Process Model
            try:
                heu_net = heuristics_miner.apply_heu(log)
                print("Heuristic Miner ile süreç modeli oluşturuldu.")
                md_file.write("## Heuristic Miner Sonuçları\n")
                md_file.write(f"{heu_net}\n\n")
                md_file.write("Heuristic Miner ile heuristik ağ (heu_net) elde edildi.\n\n")
            except Exception as e:
                error_msg = f"Heuristic Miner çalışırken hata oluştu: {e}"
                print(error_msg)
                md_file.write("## Heuristic Miner Sonuçları\n")
                md_file.write(f"**Hata:** {error_msg}\n\n")

            # 5) Directly Follows Graph çıkarma
            try:
                # Using compatible DFG discovery method
                dfg = dfg_discovery.apply(log)
                start_acts = start_activities.get_start_activities(log)
                end_acts = end_activities.get_end_activities(log)
                
                md_file.write("## Directly Follows Graph (DFG)\n")
                md_file.write("Directly Follows Graph elde edildi.\n\n")
                
                md_file.write("### Start Activities:\n")
                for activity, count in start_acts.items():
                    md_file.write(f"- {activity}: {count}\n")
                
                md_file.write("\n### End Activities:\n")
                for activity, count in end_acts.items():
                    md_file.write(f"- {activity}: {count}\n")
                
                md_file.write("\n### DFG Kenarları:\n")
                for edge, count in dfg.items():
                    md_file.write(f"- {edge} -> {count} kez gözlenmiş\n")
                md_file.write("\n")
                
                print(f"Sonuçlar '{result_file}' dosyasına kaydedildi.")
            except Exception as e:
                error_msg = f"DFG çıkartılırken hata oluştu: {e}"
                print(error_msg)
                md_file.write("## Directly Follows Graph (DFG)\n")
                md_file.write(f"**Hata:** {error_msg}\n\n")

    # 7. Inter-Dataset Transition Analizi
    print("\nInter-Dataset Transition Analizi Başlatılıyor...")
