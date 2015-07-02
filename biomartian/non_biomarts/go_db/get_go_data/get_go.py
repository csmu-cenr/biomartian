from widediaper import R


def get_go_map(outtype):

    r = R()

    r.load_library("GO.db")
    r("df <- as.data.frame(GOTERM)")
    r("colnames(df) = tolower(colnames(df))")
    r("subset_df <- subset(df, select=c('go_id', '{}'))".format(outtype))

    map_df = r.get("subset_df")

    return map_df
