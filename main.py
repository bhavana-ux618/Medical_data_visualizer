from medical_data_visualizer import draw_cat_plot, draw_heat_map

def main():
    draw_cat_plot()
    draw_heat_map()
    print("Medical Data Visualizer completed successfully.")
    print("Generated files:")
    print("- catplot.png")
    print("- heatmap.png")

if __name__ == "__main__":
    main()
